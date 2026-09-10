"""FIN 43900 Lab 06: DCF sensitivity and reverse DCF for NVIDIA."""

# Editable inputs: dollar amounts and diluted shares are in millions.
STARTING_FCFF = 96895.8470
GROWTH_RATES = [0.35, 0.25, 0.18, 0.12, 0.08]
WACC = 0.16
TERMINAL_GROWTH = 0.03
CASH = 10605.0
DEBT = 8468.0
DILUTED_SHARES = 24514.0

# Lab 06 sensitivity and reverse-DCF inputs.
SENSITIVITY_WACCS = [0.15, 0.16, 0.17]
SENSITIVITY_TERMINAL_GROWTH_RATES = [0.02, 0.03, 0.04]
TARGET_SHARE_PRICE = 218.49
REVERSE_SHIFT_LOWER = -0.05
REVERSE_SHIFT_UPPER = 0.50


def calculate_model(growth_rates, wacc, terminal_growth):
    """Return the DCF components for one set of rates."""

    if len(growth_rates) != 5:
        raise ValueError("Enter exactly five annual growth rates.")

    if any(growth_rate <= -1 for growth_rate in growth_rates):
        raise ValueError("Every annual growth rate must be greater than -100%.")

    if terminal_growth >= wacc:
        raise ValueError("Terminal growth must be less than WACC.")

    if wacc <= -1:
        raise ValueError("WACC must be greater than -100%.")

    if DILUTED_SHARES <= 0:
        raise ValueError("Diluted shares must be greater than zero.")

    forecast_fcff = []
    current_fcff = STARTING_FCFF

    for growth_rate in growth_rates:
        current_fcff *= 1 + growth_rate
        forecast_fcff.append(current_fcff)

    pv_explicit_fcff = sum(
        fcff / (1 + wacc) ** year
        for year, fcff in enumerate(forecast_fcff, start=1)
    )

    terminal_value = (
        forecast_fcff[-1]
        * (1 + terminal_growth)
        / (wacc - terminal_growth)
    )
    pv_terminal_value = terminal_value / (1 + wacc) ** 5

    enterprise_value = pv_explicit_fcff + pv_terminal_value
    equity_value = enterprise_value + CASH - DEBT
    value_per_share = equity_value / DILUTED_SHARES
    terminal_value_share = pv_terminal_value / enterprise_value

    return {
        "forecast_fcff": forecast_fcff,
        "pv_explicit_fcff": pv_explicit_fcff,
        "terminal_value": terminal_value,
        "pv_terminal_value": pv_terminal_value,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": value_per_share,
        "terminal_value_share": terminal_value_share,
    }


def calculate_dcf():
    """Calculate enterprise value, equity value, and value per share."""

    model = calculate_model(GROWTH_RATES, WACC, TERMINAL_GROWTH)

    results = [
        (f"FCFF Year {year}", fcff)
        for year, fcff in enumerate(model["forecast_fcff"], start=1)
    ]

    results.extend(
        [
            ("PV of explicit FCFF", model["pv_explicit_fcff"]),
            ("Terminal value at Year 5", model["terminal_value"]),
            ("PV of terminal value", model["pv_terminal_value"]),
            ("Enterprise value", model["enterprise_value"]),
            ("Equity value", model["equity_value"]),
            ("Value per diluted share", model["value_per_share"]),
            (
                "PV of terminal value / enterprise value",
                model["terminal_value_share"],
            ),
        ]
    )

    return results


def print_sensitivity_grid():
    """Print value per share for each WACC and terminal-growth pair."""

    print("\nSensitivity grid - value per diluted share ($)")
    first_column_width = 10
    cell_width = 12
    header = "WACC \\ g".ljust(first_column_width)
    header += "".join(
        f"{terminal_growth:.2%}".rjust(cell_width)
        for terminal_growth in SENSITIVITY_TERMINAL_GROWTH_RATES
    )
    print(header)
    print("-" * len(header))

    for sensitivity_wacc in SENSITIVITY_WACCS:
        row = f"{sensitivity_wacc:.2%}".ljust(first_column_width)
        for terminal_growth in SENSITIVITY_TERMINAL_GROWTH_RATES:
            if terminal_growth >= sensitivity_wacc:
                cell = "invalid"
            else:
                cell = (
                    f"{calculate_model(GROWTH_RATES, sensitivity_wacc, terminal_growth)['value_per_share']:.2f}"
                )
            row += cell.rjust(cell_width)
        print(row)

    base_value = calculate_model(GROWTH_RATES, WACC, TERMINAL_GROWTH)[
        "value_per_share"
    ]
    print(
        f"Base case: WACC {WACC:.2%}, terminal growth {TERMINAL_GROWTH:.2%}"
        f" -> ${base_value:.2f}"
    )


def solve_reverse_dcf():
    """Solve for a uniform shift to all five explicit growth rates."""

    lower = REVERSE_SHIFT_LOWER
    upper = REVERSE_SHIFT_UPPER

    if lower >= upper:
        raise ValueError("The reverse-DCF lower bound must be below the upper bound.")

    for bound_name, shift in (("lower", lower), ("upper", upper)):
        shifted_rates = [growth_rate + shift for growth_rate in GROWTH_RATES]
        if any(growth_rate <= -1 for growth_rate in shifted_rates):
            raise ValueError(
                f"The reverse-DCF {bound_name} bound pushes an annual growth "
                "rate to -100% or below."
            )

    def price_at_shift(shift):
        shifted_rates = [growth_rate + shift for growth_rate in GROWTH_RATES]
        return calculate_model(shifted_rates, WACC, TERMINAL_GROWTH)[
            "value_per_share"
        ]

    lower_price = price_at_shift(lower)
    upper_price = price_at_shift(upper)
    lowest_price = min(lower_price, upper_price)
    highest_price = max(lower_price, upper_price)

    if not lowest_price <= TARGET_SHARE_PRICE <= highest_price:
        return None, lower_price, upper_price

    lower_difference = lower_price - TARGET_SHARE_PRICE
    if abs(lower_difference) < 1e-10:
        return lower, lower_price, upper_price

    for _ in range(100):
        midpoint = (lower + upper) / 2
        midpoint_price = price_at_shift(midpoint)
        midpoint_difference = midpoint_price - TARGET_SHARE_PRICE

        if abs(midpoint_difference) < 1e-8:
            return midpoint, lower_price, upper_price

        if lower_difference * midpoint_difference <= 0:
            upper = midpoint
        else:
            lower = midpoint
            lower_difference = midpoint_difference

    return (lower + upper) / 2, lower_price, upper_price


def print_reverse_dcf():
    """Print the reverse-DCF solution and the assumptions held fixed."""

    solved_shift, lower_price, upper_price = solve_reverse_dcf()
    print("\nReverse DCF - uniform shift to all five explicit growth rates")
    print(f"Target share price: ${TARGET_SHARE_PRICE:.4f}")

    if solved_shift is None:
        print(
            "No solution in bracket "
            f"[{REVERSE_SHIFT_LOWER:+.2%}, {REVERSE_SHIFT_UPPER:+.2%}]."
        )
        print(
            f"Endpoint values: ${lower_price:.4f} at the lower bound; "
            f"${upper_price:.4f} at the upper bound."
        )
    else:
        solved_rates = [growth_rate + solved_shift for growth_rate in GROWTH_RATES]
        solved_price = calculate_model(solved_rates, WACC, TERMINAL_GROWTH)[
            "value_per_share"
        ]
        print(
            f"Solved uniform growth shift: {solved_shift:+.6f} "
            f"({solved_shift:+.4%}, or {solved_shift * 100:+.4f} percentage points)"
        )
        print(
            "Implied explicit growth rates: "
            + ", ".join(f"{growth_rate:.2%}" for growth_rate in solved_rates)
        )
        print(f"Model value at solved shift: ${solved_price:.4f}")

    print(
        "Held fixed: "
        f"STARTING_FCFF={STARTING_FCFF:.4f}, WACC={WACC:.4%}, "
        f"TERMINAL_GROWTH={TERMINAL_GROWTH:.4%}, CASH={CASH:.4f}, "
        f"DEBT={DEBT:.4f}, DILUTED_SHARES={DILUTED_SHARES:.4f}."
    )


if __name__ == "__main__":
    try:
        for label, value in calculate_dcf():
            print(f"{label}: {value:.4f}")
        print_sensitivity_grid()
        print_reverse_dcf()
    except ValueError as error:
        raise SystemExit(f"Error: {error}")
