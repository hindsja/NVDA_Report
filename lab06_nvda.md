# FIN 43900 Lab 06 — NVIDIA DCF

## Scope and data date

Company: NVIDIA Corporation (NASDAQ: NVDA).

The accounting inputs use NVIDIA's fiscal 2026 Form 10-K for the year ended
January 25, 2026, filed February 25, 2026. The reverse DCF uses a separate,
current market-price observation dated September 10, 2026. Mixing those dates is
required by the lab, but it means the model does not incorporate NVIDIA's later
fiscal 2027 quarterly filings.

Amounts in the model are millions of U.S. dollars, except per-share values.
Items labeled **reported** come from the filing. Items labeled **estimate** or
**forecast** are assumptions, not company guidance or reported facts.

## Inputs and sources

| Input | Value and unit | As-of date | Status and exact locator |
|---|---:|---|---|
| Starting FCFF | $96,895.847 million | Fiscal year ended Jan. 25, 2026 | **Estimate from reported inputs.** $102,718 million net cash from operating activities + $219.847 million estimated after-tax interest - $6,042 million purchases related to property, equipment, and intangible assets. Operating cash flow and capital expenditures: [FY2026 Form 10-K, Consolidated Statements of Cash Flows, p. 55](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm). The filing does not disclose cash interest paid, so $259 million interest expense from the Consolidated Statements of Income, p. 51, is used as a proxy and multiplied by (1 - 15.117%); the tax rate is $21,383 million income-tax expense / $141,450 million pretax income, Note 13, pp. 72–73. |
| Growth, Years 1–5 | 35%, 25%, 18%, 12%, 8% | Forecast for FY2027–FY2031 | **AI-assisted forecast for Jon to approve.** The path deliberately fades below NVIDIA's recent growth as scale rises. Filing anchors: fiscal 2026 revenue grew 65% in [Item 7, MD&A, pp. 36–37](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); operating cash flow rose from $64,089 million to $102,718 million and capital expenditures rose from $3,236 million to $6,042 million in the Consolidated Statements of Cash Flows, p. 55. NVIDIA does not provide a five-year FCFF forecast. |
| WACC | 16.00% | Estimated Sept. 10, 2026 | **Rounded estimate, not copied.** Detailed calculation below. Latest available 10-year Treasury par yield was 4.83% on Sept. 9 in the [U.S. Treasury daily rates table](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202609&type=daily_treasury_yield_curve). Beta was 2.22 on the [Yahoo Finance NVDA summary](https://finance.yahoo.com/quote/NVDA/) when retrieved Sept. 10. Debt and interest inputs come from the 10-K, Consolidated Statements of Income p. 51 and Note 11 p. 69. |
| Terminal growth | 3.00% | Long-run assumption after FY2031 | **Estimate.** Course-provided starting assumption from the Lab 06 “long-run economy, not the company” instruction; it is not an NVIDIA forecast. |
| Cash, debt, diluted shares | Cash $10,605 million; debt $8,468 million; diluted shares 24,514 million | Jan. 25, 2026 / fiscal 2026 | **Reported.** Cash and cash equivalents: Consolidated Balance Sheets, p. 53. Debt net carrying amount: Note 11 — Debt, p. 69. Diluted weighted-average shares: Note 4 — Net Income Per Share, p. 62. All are in the [FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm). |

The cash bridge uses only reported cash and cash equivalents. It excludes
$51,951 million of marketable securities from cash, so this is a conservative
bridge choice. Changing that definition would increase equity value by about
$2.12 per diluted share, all else equal.

### WACC calculation

The course approximation is:

`cost of equity = risk-free rate + beta × 5%`

Using a 4.83% risk-free rate and 2.22 beta gives a 15.93% cost of equity.
Pre-tax cost of debt is estimated as $259 million interest expense divided by
average debt of $8,465.5 million, or 3.06%. Applying the 15.117% effective tax
rate gives a 2.60% after-tax cost of debt.

At the $218.49 share price, equity market value is approximately
$5,356,063.86 million (`$218.49 × 24,514 million shares`). Market-value weights
are about 99.842% equity and 0.158% debt. The resulting WACC is 15.91%, rounded
to 16.00%:

`WACC = 99.842% × 15.93% + 0.158% × 2.60% = 15.91% ≈ 16.00%`

This estimate is especially sensitive to the backward-looking beta and the
course-supplied 5% equity-risk premium.

## Share-price target

The reverse-DCF target is **$218.49 per share**. The [market source reported
$218.49 at September 11, 2026, 2:03 a.m. IST](https://upstox.com/us-stocks/nvda-share-price/),
equivalent to September 10, 2026, 4:33 p.m. EDT; the page was retrieved shortly
afterward on September 10. This is a secondary-source observation rather than
an SEC fact. Jon should record a screenshot or replace it with the exact
timestamped price visible in his own market feed immediately before checkout if
it differs.

## Training-case verification completed before the company run

With the original Lab 05 inputs and a $30.00 target, `python dcf.py` preserved
the twelve known base-case lines. The added grid matched the supplied answers
cell for cell:

| WACC \ terminal growth | 2% | 3% | 4% |
|---:|---:|---:|---:|
| 9% | $28.60 | $32.94 | $39.02 |
| 10% | $24.36 | $27.50 | $31.69 |
| 11% | $21.06 | $23.41 | $26.44 |

The training reverse DCF solved a uniform growth shift of **+1.7779 percentage
points**, consistent with the expected “about +1.78 points.” Starting FCFF,
WACC, terminal growth, cash, debt, and diluted shares were held fixed.

## NVIDIA base-case DCF output

Running `python dcf.py` with the sourced and labeled NVIDIA inputs produced:

| Printed line | Model output |
|---|---:|
| FCFF Year 1 | $130,809.3935 million |
| FCFF Year 2 | $163,511.7418 million |
| FCFF Year 3 | $192,943.8553 million |
| FCFF Year 4 | $216,097.1180 million |
| FCFF Year 5 | $233,384.8874 million |
| PV of explicit FCFF | $588,359.6375 million |
| Terminal value at Year 5 | $1,849,126.4157 million |
| PV of terminal value | $880,393.1537 million |
| Enterprise value | $1,468,752.7911 million |
| Equity value | $1,470,889.7911 million |
| Value per diluted share | **$60.0020** |
| PV of terminal value / enterprise value | 59.94% |

## Sensitivity grid

Value per diluted share:

| WACC \ terminal growth | 2% | 3% | 4% |
|---:|---:|---:|---:|
| 15% | $61.86 | $65.35 | $69.47 |
| 16% | $57.11 | **$60.00** | $63.37 |
| 17% | $53.01 | $55.43 | $58.22 |

The 16% WACC / 3% terminal-growth base case is in the center. Value falls when
moving down the table as WACC rises and rises when moving right as terminal
growth rises. The corner range is **$53.01 to $69.47 per share**; the corners,
not only the middle, show the sensitivity.

## Reverse DCF

The original bracket of -5 to +10 percentage points produced no solution: its
endpoint values were $50.3051 and $84.3679, both below the $218.49 target. The
upper bound was therefore expanded to +50 points; no bound was reported as a
solution.

Within the expanded bracket, the model solves a uniform shift of **+40.7945
percentage points**. The corresponding explicit annual growth rates are
**75.79%, 65.79%, 58.79%, 52.79%, and 48.79%**.

Held fixed: starting FCFF $96,895.847 million, WACC 16.00%, terminal growth
3.00%, cash $10,605 million, debt $8,468 million, and diluted shares 24,514
million. This is one set of assumptions mathematically consistent with the
price, not proof that NVIDIA is mispriced and not a claim that the market
literally uses this forecast.

## Reasonableness

The $60.00 base-case value is 0.275× the $218.49 observed price, outside the
lab's 0.5×–2.0× reasonableness band. I did not change an input merely to force
the model toward the price.

The input I distrust most is WACC. The 16% estimate is dominated by a 2.22
backward-looking beta; because NVIDIA has almost no debt weight, that beta flows
almost directly into the discount rate. A different forward-looking beta or
equity-risk premium could materially change the value, although the sensitivity
grid still remains well below the observed price.

## Conditional recommendation

**AI-assisted draft for Jon to approve:** Watch-defer. Initiate if NVIDIA's
market price falls to approximately $60 or below without a deterioration in the
cash-flow outlook, or if sourced new evidence justifies materially higher
five-year FCFF growth than the current forecast; otherwise remain watch-defer.
Monitor one item: whether fiscal 2027 FCFF is on track to meet the model's
$130.8 billion Year 1 forecast.

## Jon's final checks before submission

- Confirm the 35% / 25% / 18% / 12% / 8% forecast reflects your own judgment and
  replace it if you cannot defend it.
- Replace the 16% WACC if your earlier WACC prediction was different; rerun the
  script and update every affected output.
- Verify the exact current NVDA price and timestamp in your market feed.
- Be prepared to explain why interest expense is only a proxy for undisclosed
  cash interest paid and why marketable securities were excluded from cash.
- Preserve this AI chat, the model/version shown by the interface, the executed
  terminal output, and your material revisions if required by the course.
