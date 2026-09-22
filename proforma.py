"""Lab 09: five-year three-statement pro-forma for the ABG known answer.

All monetary amounts are USD millions except per-share values.
Run from this folder with: python proforma.py
"""


YEARS = list(range(2026, 2031))

# Lab-provided ABG assumptions.
ORGANIC_GROWTH = 0.018
GROSS_MARGIN = 0.1705
SGA_TO_GROSS_PROFIT = dict(zip(YEARS, [0.665, 0.655, 0.645, 0.645, 0.645]))
DEPRECIATION_TO_OPENING_PPE = 82.4 / 3_070.4
ANNUAL_IMPAIRMENT = 120.0
ANNUAL_CAPEX = 250.0
TAX_RATE = 0.255
INVENTORY_DAYS = 2_135.8 / (17_999.0 - 3_071.7) * 365
FLOOR_PLAN_TO_INVENTORY = 2_027.0 / 2_135.8
OTHER_WORKING_CAPITAL_TO_REVENUE_CHANGE = 0.008
MINIMUM_CASH = 25.0
REVOLVER_LIMIT = 850.0
REVOLVER_RATE = 0.06
ANNUAL_DEBT_REPAYMENT = 150.0
ANNUAL_SHARE_BUYBACK = 150.0
FLOOR_PLAN_RATE = 0.0467
TERM_DEBT_RATE = 0.0544
COST_OF_EQUITY = 0.10
TERMINAL_GROWTH = 0.025
SHARES_OUTSTANDING = 17.951349

# FY2025 opening balance sheet and revenue.
OPENING = {
    "revenue": 17_999.0,
    "inventory": 2_135.8,
    "ppe": 3_070.4,
    "other_assets": 6_371.6,
    "cash": 40.4,
    "floor_plan": 2_027.0,
    "term_debt": 3_572.0,
    "revolver": 0.0,
    "other_liabilities": 2_127.5,
    "equity": 3_891.7,
}


def project():
    """Project the income statement, balance sheet, and cash flow in order."""
    projections = []
    prior = OPENING.copy()

    for year in YEARS:
        # Income statement: interest uses opening financing balances.
        revenue = prior["revenue"] * (1 + ORGANIC_GROWTH)
        gross_profit = revenue * GROSS_MARGIN
        sga = gross_profit * SGA_TO_GROSS_PROFIT[year]
        depreciation = prior["ppe"] * DEPRECIATION_TO_OPENING_PPE
        impairment = ANNUAL_IMPAIRMENT
        operating_income = gross_profit - sga - depreciation - impairment
        interest = (
            prior["floor_plan"] * FLOOR_PLAN_RATE
            + prior["term_debt"] * TERM_DEBT_RATE
            + prior["revolver"] * REVOLVER_RATE
        )
        pretax_income = operating_income - interest
        tax = max(0.0, pretax_income) * TAX_RATE
        net_income = pretax_income - tax

        # Balance sheet except cash.
        revenue_change = revenue - prior["revenue"]
        other_working_capital_change = (
            OTHER_WORKING_CAPITAL_TO_REVENUE_CHANGE * revenue_change
        )
        inventory = (revenue - gross_profit) * INVENTORY_DAYS / 365
        floor_plan = inventory * FLOOR_PLAN_TO_INVENTORY
        ppe = prior["ppe"] + ANNUAL_CAPEX - depreciation
        other_assets = prior["other_assets"] + other_working_capital_change - impairment
        term_debt = prior["term_debt"] - ANNUAL_DEBT_REPAYMENT
        other_liabilities = prior["other_liabilities"]
        equity = prior["equity"] + net_income - ANNUAL_SHARE_BUYBACK

        # Cash is the balancing result of all operating, investing, and financing flows.
        inventory_change = inventory - prior["inventory"]
        floor_plan_change = floor_plan - prior["floor_plan"]
        fcfe = (
            net_income
            + depreciation
            + impairment
            - ANNUAL_CAPEX
            - inventory_change
            - other_working_capital_change
            + floor_plan_change
            - ANNUAL_DEBT_REPAYMENT
        )
        cash_before_revolver = prior["cash"] + fcfe - ANNUAL_SHARE_BUYBACK

        # Draw only to meet minimum cash; otherwise repay opening revolver first.
        if cash_before_revolver < MINIMUM_CASH:
            revolver_draw = min(
                REVOLVER_LIMIT - prior["revolver"],
                MINIMUM_CASH - cash_before_revolver,
            )
            revolver = prior["revolver"] + revolver_draw
            cash = cash_before_revolver + revolver_draw
        else:
            revolver_repayment = min(
                prior["revolver"], cash_before_revolver - MINIMUM_CASH
            )
            revolver_draw = -revolver_repayment
            revolver = prior["revolver"] - revolver_repayment
            cash = cash_before_revolver - revolver_repayment

        total_assets = cash + inventory + ppe + other_assets
        total_liabilities_and_equity = (
            floor_plan
            + term_debt
            + revolver
            + other_liabilities
            + equity
        )
        balance_gap = total_assets - total_liabilities_and_equity

        result = {
            "year": year,
            "revenue": revenue,
            "gross_profit": gross_profit,
            "sga": sga,
            "depreciation": depreciation,
            "impairment": impairment,
            "operating_income": operating_income,
            "interest": interest,
            "pretax_income": pretax_income,
            "tax": tax,
            "net_income": net_income,
            "cash": cash,
            "inventory": inventory,
            "ppe": ppe,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "floor_plan": floor_plan,
            "term_debt": term_debt,
            "revolver": revolver,
            "other_liabilities": other_liabilities,
            "equity": equity,
            "total_liabilities_and_equity": total_liabilities_and_equity,
            "inventory_change": inventory_change,
            "other_working_capital_change": other_working_capital_change,
            "floor_plan_change": floor_plan_change,
            "capex": ANNUAL_CAPEX,
            "debt_repayment": ANNUAL_DEBT_REPAYMENT,
            "share_buyback": ANNUAL_SHARE_BUYBACK,
            "revolver_draw": revolver_draw,
            "fcfe": fcfe,
            "balance_gap": balance_gap,
            "cash_minimum_met": cash >= MINIMUM_CASH,
        }
        projections.append(result)
        prior = {
            "revenue": revenue,
            "inventory": inventory,
            "ppe": ppe,
            "other_assets": other_assets,
            "cash": cash,
            "floor_plan": floor_plan,
            "term_debt": term_debt,
            "revolver": revolver,
            "other_liabilities": other_liabilities,
            "equity": equity,
        }

    return projections


def print_table(title, rows, projections):
    """Print one statement with years in columns and values to one decimal."""
    label_width = 31
    print(f"\n{title} (USD millions)")
    print(f"{'Line item':<{label_width}}" + "".join(
        f"FY{item['year']}E".rjust(12) for item in projections
    ))
    print("-" * (label_width + 12 * len(projections)))
    for label, key, sign in rows:
        print(f"{label:<{label_width}}" + "".join(
            f"{sign * item[key]:>12,.1f}" for item in projections
        ))


def print_statements(projections):
    print_table("Income Statement", [
        ("Revenue", "revenue", 1),
        ("Gross profit", "gross_profit", 1),
        ("SG&A", "sga", -1),
        ("Depreciation", "depreciation", -1),
        ("Impairment", "impairment", -1),
        ("Operating income", "operating_income", 1),
        ("Interest expense", "interest", -1),
        ("Pretax income", "pretax_income", 1),
        ("Tax", "tax", -1),
        ("Net income", "net_income", 1),
    ], projections)

    print_table("Balance Sheet", [
        ("Cash", "cash", 1),
        ("Inventory", "inventory", 1),
        ("PP&E", "ppe", 1),
        ("Other assets", "other_assets", 1),
        ("Total assets", "total_assets", 1),
        ("Floor plan", "floor_plan", 1),
        ("Term debt", "term_debt", 1),
        ("Revolver", "revolver", 1),
        ("Other liabilities", "other_liabilities", 1),
        ("Equity", "equity", 1),
        ("Total liabilities & equity", "total_liabilities_and_equity", 1),
    ], projections)

    print_table("Cash Flow Statement", [
        ("Net income", "net_income", 1),
        ("Depreciation", "depreciation", 1),
        ("Impairment", "impairment", 1),
        ("Capital spending", "capex", -1),
        ("Change in inventory", "inventory_change", -1),
        ("Change in other working capital", "other_working_capital_change", -1),
        ("Change in floor plan", "floor_plan_change", 1),
        ("Debt repayment", "debt_repayment", -1),
        ("Free cash flow to equity", "fcfe", 1),
        ("Share buyback", "share_buyback", -1),
        ("Revolver draw / (repayment)", "revolver_draw", 1),
        ("Cash, year end", "cash", 1),
    ], projections)


def print_checks(projections):
    print("\nChecks")
    print(f"{'Year':<12}{'Assets - liabilities - equity':>34}{'Cash >= minimum':>22}")
    print("-" * 68)
    for item in projections:
        status = "PASS" if item["cash_minimum_met"] else "FAIL"
        print(
            f"FY{item['year']}E"
            f"{item['balance_gap']:>34,.1f}"
            f"{status:>22}"
        )


def assert_balanced(projections, tolerance=0.05):
    """Refuse valuation when a balance or minimum-cash check fails."""
    for item in projections:
        if abs(item["balance_gap"]) > tolerance:
            raise ValueError(
                f"FY{item['year']}E balance check failed: "
                f"assets - liabilities - equity = {item['balance_gap']:.1f}"
            )
        if not item["cash_minimum_met"]:
            raise ValueError(
                f"FY{item['year']}E minimum cash check failed: "
                f"cash = {item['cash']:.1f}, minimum = {MINIMUM_CASH:.1f}"
            )


def value_equity(projections):
    """Discount five FCFE values and the lab-specified terminal value."""
    present_value_fcfe = sum(
        item["fcfe"] / (1 + COST_OF_EQUITY) ** period
        for period, item in enumerate(projections, start=1)
    )
    terminal_fcfe = projections[-1]["fcfe"] + ANNUAL_DEBT_REPAYMENT
    terminal_value_2030 = (
        terminal_fcfe
        * (1 + TERMINAL_GROWTH)
        / (COST_OF_EQUITY - TERMINAL_GROWTH)
    )
    present_value_terminal = terminal_value_2030 / (1 + COST_OF_EQUITY) ** 5
    equity_value = present_value_fcfe + present_value_terminal
    share_after_2030 = present_value_terminal / equity_value
    value_per_share = equity_value / SHARES_OUTSTANDING

    print("\nEquity Valuation")
    print(f"Equity value: ${equity_value:,.2f} million")
    print(f"Share of value after 2030: {share_after_2030:.1%}")
    print(f"Value per share: ${value_per_share:,.2f}")


def main():
    projections = project()
    print_statements(projections)
    print_checks(projections)
    assert_balanced(projections)  # The model must pass before it can be valued.
    value_equity(projections)


if __name__ == "__main__":
    main()
