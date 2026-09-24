"""Lab 10: NVIDIA five-year three-statement pro-forma.

All monetary amounts are USD millions except per-share values.
The model begins with NVIDIA's FY2026 Form 10-K balance sheet and projects
FY2027-FY2031. Run from this folder with: python lab10_nvda.py

This is a course model, not investment advice. Assumptions are documented in
lab10_nvda.md and should be changed only with a stated financial reason.
"""

from copy import deepcopy
import sys


YEARS = list(range(2027, 2032))

# NVIDIA-specific revenue drivers. Data Center is projected separately because
# it represented 89.7% of FY2026 revenue and has different economics from the
# company's other end markets. Its numerical growth path reuses the prior Lab
# 06 forecast as a consistency anchor, although Lab 06 applied it to FCFF.
DATA_CENTER_GROWTH = dict(zip(YEARS, [0.35, 0.25, 0.18, 0.12, 0.08]))
OTHER_REVENUE_GROWTH = dict(zip(YEARS, [0.10, 0.10, 0.09, 0.08, 0.07]))

# Operating and balance-sheet assumptions.
GROSS_MARGIN = 0.725
R_AND_D_TO_REVENUE = dict(zip(YEARS, [0.085, 0.083, 0.081, 0.080, 0.080]))
SGA_TO_GROSS_PROFIT = dict(zip(YEARS, [0.030] * 5))
DEPRECIATION_TO_OPENING_PPE = 2_400.0 / 10_383.0
CAPEX_TO_REVENUE = 0.030
TAX_RATE = 0.150
INVENTORY_DAYS = 120.0
OTHER_WORKING_CAPITAL_TO_REVENUE_CHANGE = 0.050

# Financing and distributions.
MINIMUM_LIQUIDITY = 40_000.0
SHORT_TERM_BORROWING_LIMIT = 25_000.0
SHORT_TERM_BORROWING_RATE = 0.050
DEBT_REPAYMENT = {
    2027: 1_000.0,
    2028: 0.0,
    2029: 1_250.0,
    2030: 0.0,
    2031: 1_500.0,
}
ANNUAL_SHARE_BUYBACK = 40_000.0
ANNUAL_DIVIDEND = 1_000.0
TERM_DEBT_RATE = 259.0 / ((8_468.0 + 8_463.0) / 2.0)

# Equity valuation assumptions.
COST_OF_EQUITY = 0.1593
TERMINAL_GROWTH = 0.030
DILUTED_SHARES = 24_514.0

# FY2026 opening balance sheet and revenue from NVIDIA's FY2026 Form 10-K.
# "cash" combines cash equivalents and marketable securities because both are
# part of the liquid reserve managed by this simplified course model.
OPENING = {
    "data_center_revenue": 193_737.0,
    "other_revenue": 22_201.0,
    "revenue": 215_938.0,
    "inventory": 21_403.0,
    "ppe": 10_383.0,
    "other_assets": 112_461.0,
    "cash": 62_556.0,
    "term_debt": 8_468.0,
    "short_term_borrowing": 0.0,
    "other_liabilities": 41_042.0,
    "equity": 157_293.0,
}


def project():
    """Project the income statement, balance sheet, and cash flow in order."""
    projections = []
    prior = OPENING.copy()

    for year in YEARS:
        # Revenue and income statement. Data Center is the company-specific
        # driver; other end markets are projected separately.
        data_center_revenue = prior["data_center_revenue"] * (
            1 + DATA_CENTER_GROWTH[year]
        )
        other_revenue = prior["other_revenue"] * (1 + OTHER_REVENUE_GROWTH[year])
        revenue = data_center_revenue + other_revenue
        gross_profit = revenue * GROSS_MARGIN
        research_and_development = revenue * R_AND_D_TO_REVENUE[year]
        sga = gross_profit * SGA_TO_GROSS_PROFIT[year]
        depreciation = prior["ppe"] * DEPRECIATION_TO_OPENING_PPE
        operating_income = (
            gross_profit - research_and_development - sga - depreciation
        )
        interest_expense = (
            prior["term_debt"] * TERM_DEBT_RATE
            + prior["short_term_borrowing"] * SHORT_TERM_BORROWING_RATE
        )
        pretax_income = operating_income - interest_expense
        tax = max(0.0, pretax_income) * TAX_RATE
        net_income = pretax_income - tax

        # Balance sheet except liquidity. Capital spending is linked to revenue,
        # and inventory is linked to cost of revenue through inventory days.
        revenue_change = revenue - prior["revenue"]
        other_working_capital_change = (
            OTHER_WORKING_CAPITAL_TO_REVENUE_CHANGE * revenue_change
        )
        inventory = (revenue - gross_profit) * INVENTORY_DAYS / 365.0
        capex = revenue * CAPEX_TO_REVENUE
        ppe = prior["ppe"] + capex - depreciation
        other_assets = prior["other_assets"] + other_working_capital_change
        debt_repayment = min(DEBT_REPAYMENT[year], prior["term_debt"])
        term_debt = prior["term_debt"] - debt_repayment
        other_liabilities = prior["other_liabilities"]
        equity = (
            prior["equity"]
            + net_income
            - ANNUAL_SHARE_BUYBACK
            - ANNUAL_DIVIDEND
        )

        # Liquidity is the residual result of operating, investing, and
        # financing decisions. FCFE is before buybacks and dividends.
        inventory_change = inventory - prior["inventory"]
        fcfe = (
            net_income
            + depreciation
            - capex
            - inventory_change
            - other_working_capital_change
            - debt_repayment
        )
        liquidity_before_borrowing = (
            prior["cash"] + fcfe - ANNUAL_SHARE_BUYBACK - ANNUAL_DIVIDEND
        )

        if liquidity_before_borrowing < MINIMUM_LIQUIDITY:
            borrowing_draw = min(
                SHORT_TERM_BORROWING_LIMIT - prior["short_term_borrowing"],
                MINIMUM_LIQUIDITY - liquidity_before_borrowing,
            )
            short_term_borrowing = prior["short_term_borrowing"] + borrowing_draw
            cash = liquidity_before_borrowing + borrowing_draw
        else:
            borrowing_repayment = min(
                prior["short_term_borrowing"],
                liquidity_before_borrowing - MINIMUM_LIQUIDITY,
            )
            borrowing_draw = -borrowing_repayment
            short_term_borrowing = (
                prior["short_term_borrowing"] - borrowing_repayment
            )
            cash = liquidity_before_borrowing - borrowing_repayment

        total_assets = cash + inventory + ppe + other_assets
        total_liabilities_and_equity = (
            term_debt
            + short_term_borrowing
            + other_liabilities
            + equity
        )
        balance_gap = total_assets - total_liabilities_and_equity

        result = {
            "year": year,
            "data_center_revenue": data_center_revenue,
            "other_revenue": other_revenue,
            "revenue": revenue,
            "gross_profit": gross_profit,
            "research_and_development": research_and_development,
            "sga": sga,
            "depreciation": depreciation,
            "operating_income": operating_income,
            "interest_expense": interest_expense,
            "pretax_income": pretax_income,
            "tax": tax,
            "net_income": net_income,
            "cash": cash,
            "inventory": inventory,
            "ppe": ppe,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "term_debt": term_debt,
            "short_term_borrowing": short_term_borrowing,
            "other_liabilities": other_liabilities,
            "equity": equity,
            "total_liabilities_and_equity": total_liabilities_and_equity,
            "inventory_change": inventory_change,
            "other_working_capital_change": other_working_capital_change,
            "capex": capex,
            "debt_repayment": debt_repayment,
            "share_buyback": ANNUAL_SHARE_BUYBACK,
            "dividend": ANNUAL_DIVIDEND,
            "borrowing_draw": borrowing_draw,
            "fcfe": fcfe,
            "balance_gap": balance_gap,
            "minimum_liquidity_met": cash >= MINIMUM_LIQUIDITY,
        }
        projections.append(result)
        prior = {
            "data_center_revenue": data_center_revenue,
            "other_revenue": other_revenue,
            "revenue": revenue,
            "inventory": inventory,
            "ppe": ppe,
            "other_assets": other_assets,
            "cash": cash,
            "term_debt": term_debt,
            "short_term_borrowing": short_term_borrowing,
            "other_liabilities": other_liabilities,
            "equity": equity,
        }

    return projections


def print_table(title, rows, projections):
    """Print one statement with years in columns and values to one decimal."""
    label_width = 34
    print(f"\n{title} (USD millions)")
    print(
        f"{'Line item':<{label_width}}"
        + "".join(f"FY{item['year']}E".rjust(13) for item in projections)
    )
    print("-" * (label_width + 13 * len(projections)))
    for label, key, sign in rows:
        print(
            f"{label:<{label_width}}"
            + "".join(f"{sign * item[key]:>13,.1f}" for item in projections)
        )


def print_statements(projections):
    print_table(
        "Income Statement",
        [
            ("Data Center revenue", "data_center_revenue", 1),
            ("Other revenue", "other_revenue", 1),
            ("Revenue", "revenue", 1),
            ("Gross profit", "gross_profit", 1),
            ("Research and development", "research_and_development", -1),
            ("SG&A", "sga", -1),
            ("Depreciation", "depreciation", -1),
            ("Operating income", "operating_income", 1),
            ("Interest expense", "interest_expense", -1),
            ("Pretax income", "pretax_income", 1),
            ("Tax", "tax", -1),
            ("Net income", "net_income", 1),
        ],
        projections,
    )

    print_table(
        "Balance Sheet",
        [
            ("Cash and marketable securities", "cash", 1),
            ("Inventory", "inventory", 1),
            ("PP&E", "ppe", 1),
            ("Other assets", "other_assets", 1),
            ("Total assets", "total_assets", 1),
            ("Term debt", "term_debt", 1),
            ("Short-term borrowing", "short_term_borrowing", 1),
            ("Other liabilities", "other_liabilities", 1),
            ("Equity", "equity", 1),
            ("Total liabilities & equity", "total_liabilities_and_equity", 1),
        ],
        projections,
    )

    print_table(
        "Cash Flow Statement",
        [
            ("Net income", "net_income", 1),
            ("Depreciation", "depreciation", 1),
            ("Capital spending", "capex", -1),
            ("Change in inventory", "inventory_change", -1),
            ("Change in other working capital", "other_working_capital_change", -1),
            ("Debt repayment", "debt_repayment", -1),
            ("Free cash flow to equity", "fcfe", 1),
            ("Share buyback", "share_buyback", -1),
            ("Dividend", "dividend", -1),
            ("Borrowing draw / (repayment)", "borrowing_draw", 1),
            ("Liquidity, year end", "cash", 1),
        ],
        projections,
    )


def recompute_balance_gap(item):
    """Recompute the invariant instead of trusting a stored check value."""
    assets = item["cash"] + item["inventory"] + item["ppe"] + item["other_assets"]
    liabilities_and_equity = (
        item["term_debt"]
        + item["short_term_borrowing"]
        + item["other_liabilities"]
        + item["equity"]
    )
    return assets - liabilities_and_equity


def print_checks(projections):
    print("\nChecks")
    print(f"{'Year':<12}{'Assets - liabilities - equity':>34}{'Liquidity >= floor':>23}")
    print("-" * 69)
    for item in projections:
        gap = recompute_balance_gap(item)
        status = "PASS" if item["cash"] >= MINIMUM_LIQUIDITY else "FAIL"
        print(f"FY{item['year']}E{gap:>34,.1f}{status:>23}")


def assert_balanced(projections, tolerance=0.05):
    """Refuse valuation when a balance or minimum-liquidity check fails."""
    for item in projections:
        gap = recompute_balance_gap(item)
        if abs(gap) > tolerance:
            raise ValueError(
                f"FY{item['year']}E balance check failed: "
                f"assets - liabilities - equity = {gap:.1f}"
            )
        if item["cash"] < MINIMUM_LIQUIDITY:
            raise ValueError(
                f"FY{item['year']}E minimum liquidity check failed: "
                f"liquidity = {item['cash']:.1f}, "
                f"minimum = {MINIMUM_LIQUIDITY:.1f}"
            )


def value_equity(projections):
    """Discount five FCFE values and the course-specified terminal value."""
    present_value_fcfe = sum(
        item["fcfe"] / (1 + COST_OF_EQUITY) ** period
        for period, item in enumerate(projections, start=1)
    )
    terminal_fcfe = projections[-1]["fcfe"] + projections[-1]["debt_repayment"]
    terminal_value = (
        terminal_fcfe
        * (1 + TERMINAL_GROWTH)
        / (COST_OF_EQUITY - TERMINAL_GROWTH)
    )
    present_value_terminal = terminal_value / (1 + COST_OF_EQUITY) ** 5
    equity_value = present_value_fcfe + present_value_terminal
    share_after_explicit_period = present_value_terminal / equity_value
    value_per_share = equity_value / DILUTED_SHARES

    print("\nEquity Valuation")
    print(f"Equity value: ${equity_value:,.2f} million")
    print(
        "Share of value after FY2031: "
        f"{share_after_explicit_period:.1%}"
    )
    print(f"Value per share: ${value_per_share:,.2f}")
    return {
        "present_value_fcfe": present_value_fcfe,
        "present_value_terminal": present_value_terminal,
        "equity_value": equity_value,
        "share_after_explicit_period": share_after_explicit_period,
        "value_per_share": value_per_share,
    }


def run_rejection_test(projections):
    """Demonstrate that changing computed FY2027 liquidity is refused."""
    broken = deepcopy(projections)
    broken[0]["cash"] = OPENING["cash"]
    print("\nRejection Test")
    try:
        assert_balanced(broken)
    except ValueError as error:
        print(f"EXPECTED REFUSAL: {error}")
        return
    raise AssertionError("Rejection test failed: broken statements were accepted")


def main():
    projections = project()
    print_statements(projections)
    print_checks(projections)
    assert_balanced(projections)
    value_equity(projections)
    if "--break-test" in sys.argv:
        run_rejection_test(projections)


if __name__ == "__main__":
    main()
