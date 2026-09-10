"""FIN 43900 Lab 05: training DCF before applying the model to NVIDIA."""

  # Editable inputs: dollar amounts and diluted shares are in millions.
STARTING_FCFF = 100.0
GROWTH_RATES = [0.08, 0.06, 0.05, 0.04, 0.03]
WACC = 0.10
TERMINAL_GROWTH = 0.03
CASH = 50.0
DEBT = 300.0
DILUTED_SHARES = 50.0


def calculate_dcf():
      """Calculate enterprise value, equity value, and value per share."""

      if len(GROWTH_RATES) != 5:
          raise ValueError("Enter exactly five annual growth rates.")

      if TERMINAL_GROWTH >= WACC:
          raise ValueError("Terminal growth must be less than WACC.")

      if DILUTED_SHARES <= 0:
          raise ValueError("Diluted shares must be greater than zero.")

      # Forecast five years of free cash flow to the firm (FCFF).
      forecast_fcff = []
      current_fcff = STARTING_FCFF

      for growth_rate in GROWTH_RATES:
          current_fcff *= 1 + growth_rate
          forecast_fcff.append(current_fcff)

      # Discount the explicit five-year forecast to the valuation date.
      pv_explicit_fcff = sum(
          fcff / (1 + WACC) ** year
          for year, fcff in enumerate(forecast_fcff, start=1)
      )

      # Gordon growth terminal value at the end of Year 5.
      terminal_value = (
          forecast_fcff[-1]
          * (1 + TERMINAL_GROWTH)
          / (WACC - TERMINAL_GROWTH)
      )
      pv_terminal_value = terminal_value / (1 + WACC) ** 5

      enterprise_value = pv_explicit_fcff + pv_terminal_value
      equity_value = enterprise_value + CASH - DEBT
      value_per_share = equity_value / DILUTED_SHARES
      terminal_value_share = pv_terminal_value / enterprise_value

      results = [
          (f"FCFF Year {year}", fcff)
          for year, fcff in enumerate(forecast_fcff, start=1)
      ]

      results.extend(
          [
              ("PV of explicit FCFF", pv_explicit_fcff),
              ("Terminal value at Year 5", terminal_value),
              ("PV of terminal value", pv_terminal_value),
              ("Enterprise value", enterprise_value),
              ("Equity value", equity_value),
              ("Value per diluted share", value_per_share),
              (
                  "PV of terminal value / enterprise value",
                  terminal_value_share,
              ),
          ]
      )

      return results


if __name__ == "__main__":
      try:
          for label, value in calculate_dcf():
              print(f"{label}: {value:.4f}")
      except ValueError as error:
          raise SystemExit(f"Error: {error}")