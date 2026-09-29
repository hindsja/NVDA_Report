# Lab 11 — Locked Changed-Input Record

**Locked before the first changed-input run:** September 29, 2026, 4:59 p.m. EDT.

This record is AI-assisted under the instructor exception communicated for this
lab. It was saved before any lower or higher Lab 11 sensitivity case was run.
The unchanged Lab 10 base was run first and produced FY2031 operating income of
$303,302.5 million, FY2031 FCFE of $244,585.5 million, and value of $62.97 per
share, with all accounting checks passing.

## Inputs and prediction locked before execution

### Driver 1 — Data Center revenue growth

- Base FY2027–FY2031 path: 35%, 25%, 18%, 12%, 8%.
- Lower path: 30%, 20%, 13%, 7%, 3%, a 5-percentage-point decrease in every
  forecast year.
- Higher path: 40%, 30%, 23%, 17%, 13%, a 5-percentage-point increase in every
  forecast year.
- Range reason: Lab 10 labels the fading path as judgment and reports that
  historical Data Center growth slowed from 217% to 142% to 68%. A symmetric
  five-point shift tests meaningful forecast error without replacing the
  original fade pattern.
- Prediction: the lower path will reduce each later year's Data Center revenue,
  so the effect will compound through revenue, gross profit, operating income,
  net income, and FCFE. The higher path will reverse those directions. The
  FY2031 operating-income and FCFE effects should be in the tens of billions of
  dollars, and value per share could move by roughly $10–$20 in either direction.

### Driver 2 — Gross margin

- Base FY2027–FY2031 value: 72.5% each year.
- Lower value: 70.0% each year, a 2.5-percentage-point decrease.
- Higher value: 75.0% each year, a 2.5-percentage-point increase.
- Range reason: reported FY2024–FY2026 gross margins were 72.72%, 74.99%, and
  71.07%. The high case approximates the historical peak. The 70.0% low case is
  modestly below recent history and approximately applies the FY2026 filing's
  disclosed 2.6-percentage-point unfavorable effect from inventory and excess
  purchase-obligation provisions to the 72.5% base.
- Prediction: lower margin will reduce gross profit and operating income at the
  same revenue, with most of the after-tax effect flowing to FCFE; higher margin
  will reverse those directions. Because SG&A equals 3% of gross profit, the
  operating-income response will be slightly smaller than the direct gross-profit
  change. FY2031 operating income should move by roughly $12 billion in either
  direction, FCFE by roughly $10 billion, and value per share by roughly $3–$5.

### Predicted ranking

Over these chosen ranges, the Data Center growth path is expected to create the
larger span in final-year operating income, final-year FCFE, and value per share
because its five annual changes compound. This is a range-dependent prediction,
not a claim that growth is always intrinsically more important than margin.

## Post-run reconciliation

Added after executing `python lab11_nvda.py`:

| Driver and case | FY2031 operating income | Change from base | FY2031 FCFE | Change from base | Value/share | Change from base |
|---|---:|---:|---:|---:|---:|---:|
| Data Center growth — lower | $247,884.5 million | −$55,418.0 million | $202,671.9 million | −$41,913.6 million | $54.03 | −$8.94 |
| Data Center growth — base | $303,302.5 million | $0.0 | $244,585.5 million | $0.0 | $62.97 | $0.00 |
| Data Center growth — higher | $368,924.6 million | +$65,622.0 million | $293,666.5 million | +$49,081.0 million | $73.29 | +$10.32 |
| Gross margin — lower | $291,166.0 million | −$12,136.5 million | $233,967.2 million | −$10,618.3 million | $60.13 | −$2.85 |
| Gross margin — base | $303,302.5 million | $0.0 | $244,585.5 million | $0.0 | $62.97 | $0.00 |
| Gross margin — higher | $315,439.0 million | +$12,136.5 million | $255,203.8 million | +$10,618.3 million | $65.82 | +$2.85 |

The predicted direction and ranking were correct. The growth prediction correctly
anticipated effects in the tens of billions; its actual value-per-share change
was −$8.94 to +$10.32, near the lower edge of the predicted roughly $10–$20
change. The margin prediction was accurate for operating income (±$12.14
billion) and FCFE (±$10.62 billion), while the ±$2.85 per-share result was
slightly smaller than the predicted roughly $3–$5.

The higher growth case had a larger absolute gain than the lower case's loss
because changing a percentage growth path affects an expanding revenue base and
compounds multiplicatively across five years. That nonlinearity was not stated
in the initial prediction.

The result does not change the prior watch-defer valuation conclusion: even the
higher-growth case produces $73.29 per share, still far below the prior Lab 10
market observation of $224.58 on September 24, 2026. It does change the research
priority by making support for the Data Center growth path more important than
refining gross margin within the tested range. This conclusion is explicitly
limited to these ranges.
