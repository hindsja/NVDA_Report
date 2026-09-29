# Lab 11 — NVIDIA Pro-Forma Sensitivity

**Question:** Which assumptions drive NVIDIA's forecast and value, and what
explains their effects?

**Company:** NVIDIA Corporation (NVDA). **Analysis date:** September 29, 2026.
Monetary amounts are USD millions except per-share values. The analysis extends
the preserved [`lab10_nvda.py`](lab10_nvda.py) model through
[`lab11_nvda.py`](lab11_nvda.py). Full executed output is retained in
[`outputs/lab11_output.txt`](outputs/lab11_output.txt), and the timestamped
prediction plus reconciliation is in
[`lab11_locked_record.md`](lab11_locked_record.md).

This is AI-assisted course analysis.

## Base and selected operating drivers

The unchanged Lab 10 base produced FY2031 operating income of **$303,302.5
million**, FY2031 free cash flow to equity (**FCFE**) of **$244,585.5 million**,
and **$62.97 per share**. All five balance-sheet and liquidity checks passed.

| Independent driver | Lower | Base | Higher | Units and affected years | Range reason |
|---|---|---|---|---|---|
| Data Center revenue growth | 30%, 20%, 13%, 7%, 3% | 35%, 25%, 18%, 12%, 8% | 40%, 30%, 23%, 17%, 13% | Annual growth rates for FY2027–FY2031; ±5 percentage points in each year | Lab 10 labels the fading path as judgment and reports historical Data Center growth slowing from 217% to 142% to 68%. A symmetric shift preserves the path's shape while testing forecast error. |
| Gross margin | 70.0% | 72.5% | 75.0% | Percent of revenue in FY2027–FY2031; ±2.5 percentage points | Reported FY2024–FY2026 margins were 72.72%, 74.99%, and 71.07%. The high case approximates the peak; the low case is modestly below recent history and approximates applying the disclosed 2.6-point FY2026 provision headwind to the base. |

The locked prediction expected Data Center growth to be the larger driver over
these ranges because annual growth changes compound. It predicted roughly
±$12 billion of FY2031 operating-income effect from margin and effects in the
tens of billions from the growth path.

## Method

This is one-at-a-time sensitivity analysis: each lower, base, or higher run
starts with a fresh deep copy of the complete Lab 10 base input set. The code
changes only the named driver, reruns all five linked income statements, balance
sheets, cash-flow statements, and the existing FCFE valuation, and independently
recomputes the accounting checks. A control identifies every changed top-level
independent input; any unexpected change invalidates the run. Changed outputs
equal the changed result minus the common base result, and each span equals the
maximum minus the minimum valid result.

## Sensitivity results

### Data Center revenue growth

| Case | FY2031 operating income | Change from base | FY2031 FCFE | Change from base | Value/share | Change from base | Checks |
|---|---:|---:|---:|---:|---:|---:|---|
| Lower | $247,884.5 | −$55,418.0 | $202,671.9 | −$41,913.6 | $54.03 | −$8.94 | Pass |
| Base | $303,302.5 | $0.0 | $244,585.5 | $0.0 | $62.97 | $0.00 | Pass |
| Higher | $368,924.6 | +$65,622.0 | $293,666.5 | +$49,081.0 | $73.29 | +$10.32 | Pass |
| **Span** | **$121,040.0** |  | **$90,994.5** |  | **$19.26** |  |  |

### Gross margin

| Case | FY2031 operating income | Change from base | FY2031 FCFE | Change from base | Value/share | Change from base | Checks |
|---|---:|---:|---:|---:|---:|---:|---|
| Lower | $291,166.0 | −$12,136.5 | $233,967.2 | −$10,618.3 | $60.13 | −$2.85 | Pass |
| Base | $303,302.5 | $0.0 | $244,585.5 | $0.0 | $62.97 | $0.00 | Pass |
| Higher | $315,439.0 | +$12,136.5 | $255,203.8 | +$10,618.3 | $65.82 | +$2.85 | Pass |
| **Span** | **$24,273.0** |  | **$21,236.7** |  | **$5.69** |  |  |

## Trace of a changed result

The higher Data Center growth case shows the causal link. Faster annual growth
raises Data Center revenue and total revenue. At the unchanged 72.5% gross
margin, gross profit rises; linked R&D, SG&A, capital spending, inventory, and
working capital also recalculate. The net effect increases operating income,
net income, and FCFE rather than treating revenue as a stand-alone change.

| Year | Data Center growth | Data Center revenue | Total revenue | Gross profit | Operating income | Net income | FCFE | Balance gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| FY2027E | 40.0% | $271,231.8 | $295,652.9 | $214,348.4 | $180,387.4 | $153,109.1 | $136,326.5 | $0.0 |
| FY2028E | 30.0% | $352,601.3 | $379,464.6 | $275,111.8 | $231,467.5 | $196,553.1 | $177,296.5 | $0.0 |
| FY2029E | 23.0% | $433,699.6 | $462,980.5 | $335,660.9 | $282,463.3 | $239,899.6 | $218,660.0 | $0.0 |
| FY2030E | 17.0% | $507,428.6 | $539,052.0 | $390,812.7 | $328,427.8 | $279,001.9 | $259,685.4 | $0.0 |
| FY2031E | 13.0% | $573,394.3 | $607,231.3 | $440,242.7 | $368,924.6 | $313,424.2 | $293,666.5 | $0.0 |

## Validation

| Check | Executed result |
|---|---|
| First base versus Lab 10 | Exact match at displayed precision: $303,302.5 operating income, $244,585.5 FCFE, and $62.97/share |
| Only selected input changed | Pass for all lower and higher cases; base cases reported no changes |
| Linked recalculation | Complete five-year model reran for every case |
| Accounting and liquidity | Maximum displayed balance gap was $0.0; liquidity passed in all six runs |
| Change from base | Computed in code as changed output minus first base output |
| Restored base inputs | Exact match to the first base |
| Restored base outputs | Exact match to the first base |

An additional independent programmatic comparison confirmed that the Lab 11
base reproduces every shared numeric statement line from the Lab 10 model.

## Main driver over the tested ranges

**Over these ranges, the Data Center growth path is the larger driver of all
three outputs.** Its $121,040.0 million operating-income span is about five times
the $24,273.0 million margin span. Its $90,994.5 million FCFE span and $19.26
per-share valuation span also exceed the margin spans of $21,236.7 million and
$5.69 per share.

The mechanism is compounding. Every annual growth change affects the following
year's revenue base, then passes through gross profit and the linked operating,
reinvestment, working-capital, and tax lines. Gross margin has a strong direct
effect, but it does not change the revenue base. The growth result is asymmetric:
the high case adds more than the low case subtracts because percentage growth
compounds multiplicatively on different revenue levels.

This ranking is not universal. The growth path moves by five percentage points
in each of five years, while margin moves by 2.5 points; a wider margin range or
narrower growth range could alter the ranking. Raw dollar spans also should not
be used to rank sensitivity across unlike companies.

## Prediction reconciliation and decision relevance

The predicted directions and ranking were correct. Growth produced the expected
tens-of-billions effect, while margin moved FY2031 operating income by
±$12,136.5 million and FCFE by ±$10,618.3 million. The margin value response of
±$2.85 per share was slightly smaller than the predicted roughly $3–$5. The
growth valuation response, −$8.94 to +$10.32, was near the low end of the
predicted roughly $10–$20 magnitude. The unpredicted detail was the growth
case's asymmetry caused by multiplicative compounding.

The result does **not** change the prior watch-defer conclusion. Even the tested
higher-growth case produces $73.29 per share, far below the Lab 10 market
observation of $224.58 on September 24, 2026. It does make support for the Data
Center growth path the first research priority: the next work should test demand,
capacity, customer concentration, inventory provisions, and the durability of
AI infrastructure spending. This is not an investment recommendation.

## Sensitivity concepts

**What is one-at-a-time sensitivity?** It changes one independent assumption,
holds every other independent input at base, and lets all linked formulas
recalculate. It isolates the model's response to that one selected change, but
it does not capture interactions between drivers.

**How does the input range affect the ranking?** A span combines model
sensitivity with the width of the tested range. A driver can appear more
important simply because its lower and higher cases are farther from base.
Rankings therefore must be stated as applying “over these ranges.”

**Why is this not a forecast probability?** Lower, base, and higher are
conditional cases, not estimated probabilities. The table does not say how
likely each input is, define a statistical distribution, or combine correlated
changes. It answers “what if this input changes?” rather than “how likely is
this outcome?”

**Reflection:** Over the selected ranges, Data Center growth mattered most. The
most notable result was that five modest annual shifts compounded into a
$121.0 billion FY2031 operating-income span, while even the higher-growth value
remained far below the prior market observation.

## Limitations and AI record

- The sensitivity inherits all Lab 10 model limitations, including its fixed
  share count, simplified working-capital accounts, and terminal-value method.
- One-at-a-time cases exclude interaction between growth and margin. In practice,
  faster growth could raise or lower margins and reinvestment needs.
- The tested ranges are judgments supported by prior work, not probability
  intervals or company guidance.
- The cost of equity and terminal growth remain fixed, so this lab isolates
  operating drivers rather than every valuation assumption.

The model, prompt context, locked record, executed output, checks, ranges, and
material interpretation changes should be retained with the course AI-use
record.

