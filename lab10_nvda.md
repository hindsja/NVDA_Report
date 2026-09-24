# Lab 10 — NVIDIA Pro-Forma

**Question:** What are five years of NVIDIA's statements worth, built from assumptions that can be defended?

**Company:** NVIDIA Corporation (**NVDA**). **Analysis date:** September 24, 2026. Monetary amounts are USD millions unless stated otherwise. The five-year model is in [`lab10_nvda.py`](lab10_nvda.py).

## Company-specific line

NVIDIA's Data Center revenue is the company-specific line: it supplied 89.7% of fiscal 2026 revenue, so the model forecasts Data Center and all other end markets separately instead of applying one growth rate to the whole company. Research and development (R&D) is also shown separately because NVIDIA is a fabless platform designer whose product cadence depends on sustained design, software, and compute spending.

This is an AI-assisted proposal for course analysis, not company guidance or an investment recommendation. Judgment reasons should be retained only if the student understands and can defend them.

## Three-year filing history

Each fiscal year below is traced to its own Form 10-K: [FY2024 Form 10-K, accession 0001045810-24-000029, filed February 21, 2024](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm); [FY2025 Form 10-K, accession 0001045810-25-000023, filed February 26, 2025](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm); and [FY2026 Form 10-K, accession 0001045810-26-000021, filed February 25, 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm).

| Required history item | FY2024 | Filing | FY2025 | Filing | FY2026 | Filing |
|---|---:|---|---:|---|---:|---|
| Revenue | 60,922 | FY2024 10-K, income statement | 130,497 | FY2025 10-K, income statement | 215,938 | FY2026 10-K, income statement |
| Gross profit | 44,301 | FY2024 10-K, income statement | 97,858 | FY2025 10-K, income statement | 153,463 | FY2026 10-K, income statement |
| SG&A | 2,654 | FY2024 10-K, income statement | 3,491 | FY2025 10-K, income statement | 4,579 | FY2026 10-K, income statement |
| Net income | 29,760 | FY2024 10-K, income statement | 72,880 | FY2025 10-K, income statement | 120,067 | FY2026 10-K, income statement |
| Inventory | 5,282 | FY2024 10-K, balance sheet | 10,080 | FY2025 10-K, balance sheet | 21,403 | FY2026 10-K, balance sheet |
| PP&E, net | 3,914 | FY2024 10-K, balance sheet | 6,283 | FY2025 10-K, balance sheet | 10,383 | FY2026 10-K, balance sheet |
| Shareholders' equity | 42,978 | FY2024 10-K, balance sheet | 79,327 | FY2025 10-K, balance sheet | 157,293 | FY2026 10-K, balance sheet |

The FY2026 10-K's comparative income statement independently repeats the FY2024 and FY2025 income-statement values, and its cash-flow statement reports exact depreciation and amortization of 1,508, 1,864, and 2,843. For the requested depreciation-to-PP&E ratio, the PP&E note's narrower depreciation expense is used: $894 million, approximately $1.3 billion, and approximately $2.4 billion.

### Student filing checks required by the lab

These checks must be performed personally; AI source review does not count as the student's two hand checks.

| Suggested check | Filing location | Student confirmation |
|---|---|---|
| FY2026 revenue = 215,938 | FY2026 10-K, Consolidated Statements of Income | [add checked date and initials] |
| FY2026 inventory = 21,403 | FY2026 10-K, Consolidated Balance Sheets | [add checked date and initials] |

No required history item remains unresolved in the AI extraction. The two student confirmations remain incomplete until recorded above.

## Historical ratios and provider cross-check

Inventory days use ending inventory divided by cost of revenue times 365, matching the course video. Depreciation uses the PP&E note's depreciation expense divided by ending net PP&E, also matching the video's convention. Growth is year-over-year reported consolidated growth; FY2024 compares with FY2023 revenue of 26,974.

| Ratio or cross-check | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| Reported revenue growth | 125.9% | 114.2% | 65.5% |
| Organic / same-store / comparable growth | Not disclosed | Not disclosed | Not disclosed |
| Gross margin | 72.72% | 74.99% | 71.07% |
| SG&A / gross profit | 5.99% | 3.57% | 2.98% |
| Inventory days | 116.0 | 112.7 | 125.0 |
| Depreciation / ending PP&E | 22.84% | 20.69% | 23.11% |
| Capital spending — filing | 1,069 | 3,236 | 6,042 |
| Capital expenditure — [Yahoo Finance standardized field](https://finance.yahoo.com/quote/NVDA/cash-flow/) | (1,069) | (3,236) | (6,042) |
| Effective tax rate | 12.00% | 13.26% | 15.12% |

The provider and filing capital-spending amounts agree in magnitude; the provider displays capital expenditure as a negative cash outflow. This is the only provider-derived cross-check in the analysis, it is not used as a model input, and the SEC filing values control. NVIDIA does not disclose an organic, same-store, or comparable-company growth measure in these MD&A sections. Reported growth is therefore kept as reported growth and is not relabeled organic.

Data Center revenue was 47,525, 115,186, and 193,737 in FY2024–FY2026. The related reported growth rates were 217%, 142%, and 68%, respectively. The FY2026 filing also says inventory and excess purchase-obligation provisions had a 2.6-percentage-point unfavorable effect on gross margin, which matters when selecting a forward margin.

## Cross-reference to the local EDGAR filing and prior NVIDIA labs

The primary recheck used the locally saved `nvda-20260125.html`, not a provider export. Its income statement, balance sheet, cash-flow statement, debt note, EPS note, and end-market table reproduce the figures previously used in Labs 06 and 08.

| Item | Local FY2026 EDGAR filing | Prior saved work | Lab 10 treatment |
|---|---:|---|---|
| Revenue | 215,938 | Project file and Lab 08: 215,938 | FY2026 opening revenue; exact match |
| Data Center revenue | 193,737 | Project file and Lab 08: 193,737, or 89.7% of revenue | Separate company-specific revenue driver; exact match |
| Net income | 120,067 | Project file: 120,067 | Historical reasonableness anchor; exact match |
| Operating cash flow | 102,718 | Lab 06 starting-FCFF calculation: 102,718 | Cross-check only; Lab 10 forecasts FCFE from linked statements |
| Capital spending | 6,042 | Lab 06: 6,042 | Filing value anchors the 3.0%-of-revenue forecast |
| Cash and cash equivalents | 10,605 | Lab 06 equity bridge: 10,605 | Included in Lab 10 liquidity |
| Marketable securities | 51,951 | Lab 06 disclosed but deliberately excluded from its cash bridge | Combined with cash in Lab 10 so the opening balance sheet and liquidity reserve include both reported liquid lines |
| Debt, net carrying amount | 8,468 | Lab 06: 8,468 | FY2026 opening term debt; exact match |
| Diluted weighted-average shares | 24,514 | Labs 06 and 08: 24,514 | Fixed valuation denominator; exact match |
| Diluted EPS | 4.90 | Lab 08: 4.90 | Cross-check only; not a pro-forma input |
| Cost of equity | Filing does not report it | Lab 06 CAPM estimate: 15.93% | FCFE discount rate; corrected from the rounded 16.00% FCFF WACC |
| WACC | Filing does not report it | Lab 06: 15.91%, rounded to 16.00% | Not used because Lab 10 values equity cash flow, not enterprise cash flow |
| Terminal growth | Filing does not report it | Lab 06 judgment: 3.00% | Reused unchanged |
| Five-year growth path | Filing does not provide a five-year forecast | Lab 06: 35%, 25%, 18%, 12%, 8% for FCFF | Reused as a numerical anchor for Data Center revenue, but relabeled as a new judgment because revenue growth and FCFF growth are not the same variable |

Lab 06 calculated starting FCFF as `102,718 operating cash flow + 219.847 after-tax interest − 6,042 capital spending = 96,895.847`. The local EDGAR filing confirms the reported operating cash flow, $259 interest expense, capital spending, and 15.117% effective tax rate underlying that calculation.

The liquidity definitions differ intentionally rather than contradicting each other. Lab 06 used only 10,605 of cash in its enterprise-to-equity bridge and disclosed that excluding 51,951 of marketable securities was conservative. Lab 10 needs a complete opening balance sheet and therefore combines the two reported liquid-asset lines into 62,556; it does not add that opening liquidity separately to the FCFE valuation.

## Opening FY2026 balance sheet

The model combines cash equivalents and marketable securities into one liquidity line. Other assets and other liabilities are explicit residual groupings so the opening balance sheet reconciles exactly.

| Opening asset | Value | Opening liability or equity | Value |
|---|---:|---|---:|
| Cash and cash equivalents + marketable securities | 62,556 | Term debt | 8,468 |
| Inventory | 21,403 | Short-term model borrowing | 0 |
| PP&E, net | 10,383 | Other liabilities | 41,042 |
| Other assets | 112,461 | Shareholders' equity | 157,293 |
| **Total assets** | **206,803** | **Total liabilities and equity** | **206,803** |

The asset residual is `206,803 − 62,556 − 21,403 − 10,383 = 112,461`. The liability residual is `49,510 total liabilities − 8,468 debt = 41,042`.

## Labelled assumption set

| Assumption | Value | Label | Reason |
|---|---:|---|---|
| Data Center revenue growth, FY2027–FY2031 | 35%, 25%, 18%, 12%, 8% | Judgment | The numerical path is carried from Lab 06 for consistency, but it becomes a new judgment because that lab applied it to FCFF. Reported Data Center growth slowed from 217% to 142% to 68%, supporting a fade as scale and operating risks increase. |
| Other-revenue growth, FY2027–FY2031 | 10%, 10%, 9%, 8%, 7% | Judgment | Gaming, Professional Visualization, Automotive, and OEM are smaller and less concentrated in the AI infrastructure buildout, so they receive a lower growth path than Data Center. |
| Gross margin | 72.5% | Judgment | The three-year reported range was 71.1%–75.0%; 72.5% is above FY2026's charge-affected result but below FY2025's peak. |
| R&D / revenue, FY2027–FY2031 | 8.5%, 8.3%, 8.1%, 8.0%, 8.0% | Judgment | FY2026 R&D was 8.6% of revenue. The ratio declines only gradually because annual platform development and compute infrastructure remain essential even as revenue scales. |
| SG&A / gross profit | 3.0% | History | FY2026 was 2.98%, after falling from 5.99% in FY2024 and 3.57% in FY2025. |
| Depreciation / opening PP&E | 23.11% | History | FY2026 PP&E-note depreciation of approximately 2,400 divided by ending net PP&E of 10,383. |
| Capital spending / revenue | 3.0% | Judgment | Filing capital spending rose from 1.75% to 2.48% to 2.80% of revenue, and management expects FY2027 capital spending to increase; 3.0% carries that direction without inventing dollar guidance. |
| Tax rate | 15.0% | History | FY2026's effective rate was 15.12%, up from 12.00% and 13.26% in the prior two years. |
| Inventory days | 120 days | Judgment | The three-year average was 117.9 days; 120 stays near that history while recognizing the larger Blackwell supply ramp and recent inventory provisions. |
| Floor plan | None | History | NVIDIA is not a vehicle dealer and its 10-K does not report floor-plan inventory financing. Inventory is funded through ordinary liquidity and liabilities. |
| Other working capital | 5.0% of change in revenue | Judgment | FY2026 non-inventory operating working capital—receivables plus prepaid assets less accounts payable and accrued current liabilities—was about 4.9% of revenue; 5.0% is a simple linked approximation. |
| Minimum liquidity | 40,000 | Judgment | This is below the 62,556 opening cash-and-marketable-securities balance but retains a substantial reserve against NVIDIA's manufacturing, cloud, and investment commitments. |
| Short-term borrowing limit | 25,000 | History | The FY2026 10-K reports a $25.0 billion commercial-paper program and no amount outstanding at year-end; this is a borrowing backstop, not a dealer floor plan. |
| Short-term borrowing rate | 5.0% | Judgment | No borrowing was outstanding at year-end, so the model uses a conservative round rate if the liquidity floor ever requires a draw. |
| Debt repayment, FY2027–FY2031 | 1,000; 0; 1,250; 0; 1,500 | History | The schedule follows the 10-K's notes due in calendar 2026, 2028, and 2030, mapped to NVIDIA fiscal years. |
| Term-debt interest rate | 3.06% | History | FY2026 interest expense of 259 divided by average FY2025/FY2026 debt of 8,465.5. |
| Annual share buyback | 40,000 | Judgment | FY2026 cash payments for repurchases were 40,086 and shares repurchased reduced equity by 40,388; the model carries a rounded amount rather than assuming continued acceleration. |
| Annual dividend | 1,000 | Judgment | FY2026 dividends were 974; 1,000 is a rounded continuation and not a board commitment. |
| Cost of equity | 15.93% | Judgment | Lab 06's CAPM calculation produced 15.93%. Its 15.91% WACC was rounded to 16.00% for FCFF, but Lab 10 discounts FCFE and therefore uses the cost of equity directly. |
| Terminal growth | 3.0% | Judgment | A long-run nominal economic-growth assumption carried from the prior DCF, not an NVIDIA forecast. |
| Valuation share count | 24,514 million | History | FY2026 diluted weighted-average shares from Note 4; using a fixed count does not credit future buybacks with reducing shares. |

## Model implementation and executed result

The model calculates revenue and income first, then all balance-sheet lines except liquidity, then free cash flow to equity (FCFE), and finally liquidity. Data Center and other revenue drive total revenue. R&D reduces operating income, inventory follows cost of revenue and days, and capital spending follows revenue. The balance-sheet identity and minimum-liquidity condition must pass before valuation runs.

Executed with:

```powershell
python lab10_nvda.py --break-test
```

| Model line | FY2027E | FY2031E |
|---|---:|---:|
| Revenue | 285,966.0 | 500,475.0 |
| Operating income | 174,398.5 | 303,302.5 |
| Net income | 148,018.5 | 257,645.4 |
| Free cash flow to equity | 132,886.7 | 244,585.5 |
| Cash and marketable securities | 154,442.7 | 825,437.9 |
| Assets − liabilities − equity | 0.0 | 0.0 |

All five annual balance gaps printed **0.0**, and liquidity passed the 40,000 floor in every year. No short-term borrowing was drawn because operating FCFE remained above buybacks, dividends, and the liquidity requirement.

The discounted equity value is **$1,543,651.91 million**, or **$62.97 per share** using 24,514 million diluted shares. The discounted terminal value supplies **60.6%** of total modeled equity value. The result is close to Lab 06's $60.0020 FCFF DCF, but it is not independent confirmation because the models share the prior growth path, discount-rate work, terminal growth, filing, and share count.

The rejection test replaces computed FY2027 liquidity with the opening 62,556 while leaving the projected activity in place. The model refuses valuation and reports:

```text
EXPECTED REFUSAL: FY2027E balance check failed: assets - liabilities - equity = -91886.7
```

The gap equals the omitted FY2027 increase in liquidity with the sign reversed, so it points directly to the broken liquidity roll-forward.

## Model value and market price

The latest market-data quote retrieved for September 24, 2026 was **$224.58 per share at 4:29 p.m. EDT**; it is a market quote rather than a filing fact. The [Nasdaq NVDA page](https://www.nasdaq.com/market-activity/stocks/nvda) is the price locator.

**Same-share-count comparison:** the model says **$62.97 per share**, or $1.544 trillion on 24.514 billion shares, while the market quote says **$224.58 per share**, or $5.505 trillion on the same share count—what combination of sustainable Data Center growth, margins, and cost of equity would have to explain the difference?

## Organic growth

Organic growth is growth produced by the businesses already owned, excluding acquisitions, divestitures, and often currency effects. NVIDIA's three MD&A disclosures report consolidated and end-market growth but do not label an organic, same-store, or comparable measure, so no organic figure is invented.

For the ABG course case, reported revenue grew 4.7%, but stores already owned grew about 1.2%; acquisitions created much of the difference. The video carries 1.8% because it forecasts the existing store base slightly above the disclosed same-store result and excludes unmodeled acquisitions and their purchase prices.

## Limitations

- The forecast is a simplified course model, not a full GAAP forecast. NVIDIA allocates depreciation within functional expenses, while the course engine displays depreciation separately; this can create classification differences from reported operating expenses.
- Existing cash and marketable securities support the opening balance sheet but are not separately added to the FCFE valuation. The model also omits interest income and volatile investment gains.
- The fixed 24,514 million diluted-share denominator does not assume future buybacks reduce shares, even though cash buybacks reduce projected equity and liquidity.
- Other assets and liabilities are broad residual groupings. Acquisitions, stock-based compensation, deferred taxes, leases, commitments, and individual working-capital accounts are not forecast separately.
- The 15.93% cost of equity and the fading Data Center growth path drive much of the result. A conclusion should not be drawn from the point estimate without sensitivity analysis.

## Partner fresh-eyes review — student evidence required

The following entries must record the actual partner exchange. They are intentionally not invented by AI.

**Partner's attack on one judgment:** Why did you reuse the FCFF growth path from Lab 06 as Data Center revenue growth when revenue and FCFF are different measures, and what evidence would make you change it?

**Two-sentence response:** I reused the path as a consistency anchor, not as a filing fact, and labeled it judgment because Data Center growth has already slowed from 217% to 142% to 68% as the revenue base expanded. I would lower the forecast if future filings showed weaker hyperscaler demand, slower Data Center growth, rising inventory provisions, or margin pressure; I would raise it only with sustained demand and capacity evidence.

**Specific attack given to the partner:** Why did you apply one consolidated growth or margin assumption to Amazon instead of separating AWS from the lower-margin retail businesses, and how could that choice bias the resulting value per share?

## AI use and verification

Lab 10 was created with educational AI assistance.
