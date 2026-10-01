# Lab 12 — NVIDIA Full-Analysis Review

**Decision question:** How did I get from choosing NVIDIA to my valuation
conclusion, which assumptions drive it, and what evidence could change my
mind?

**Current conclusion:** **Watch-defer.** The most recent saved market
observation is **$224.58 per common share on September 24, 2026**, while the
five-year FCFE pro-forma produces **$62.97 per diluted share** and the earlier
FCFF DCF produces **$60.00 per diluted share**. Lab 11's tested operating cases
range from **$54.03 to $73.29 per diluted share**. The peer P/E exercise gives a
much higher mechanical span of **$370.66–$931.18 per common share**, but its two
peers have materially different business mixes and stale annual GAAP earnings.
I do not average these conflicting methods. The disagreement is evidence that
the conclusion depends on the forward operating path, the discount rate, and
peer comparability.

All monetary statement amounts below are millions of U.S. dollars unless
stated otherwise. This review uses existing work and saved outputs; it does not
claim a new valuation date or a new market-price observation.

## Evidence open for the presentation

- [Initial target analysis and research plan](nvdalab3.md)
- [FY2026 FCFF DCF, sensitivity, and reverse DCF](lab06_nvda.md) and
  [calculator](dcf.py)
- [Peer P/E analysis](lab08_nvda.md) and [calculator](lab08_pe.py)
- [Five-year NVIDIA pro-forma](lab10_nvda.md) and [model](lab10_nvda.py)
- [Lab 11 sensitivity analysis](lab11_nvda.md),
  [model](lab11_nvda.py), [locked record](lab11_locked_record.md), and
  [executed output](outputs/lab11_output.txt)
- [NVIDIA FY2026 Form 10-K saved locally](nvda-20260125.html)

## Presentation route

### 1. Target selection

I selected NVIDIA because its operating performance is strong, its value is
concentrated in an identifiable company-specific driver, and its market price
requires a demanding valuation test. NVIDIA's FY2026 Data Center revenue was
$193,737 out of $215,938 of total revenue, or 89.7%. That makes Data Center
demand central to both the upside and the risk. The same filing supplies
reported statements, end-market revenue, debt, diluted shares, commitments,
and customer-concentration evidence, so the company is suitable for a
source-traceable model.

My initial view was watch-defer. Strong growth, profitability, and liquidity
did not by themselves establish that the shares offered an adequate expected
return. I wanted a price-based DCF, peer comparison, linked pro-forma, and
sensitivity analysis before considering initiation. The analysis has made that
view more specific but has not changed it.

### 2. Company and evidence

NVIDIA earns money by selling accelerated-computing and networking platforms,
including GPUs, CPUs, interconnects, systems, and software. Data Center is the
dominant end market. The main historical source is NVIDIA's FY2026 Form 10-K for
the fiscal year ended January 25, 2026 and filed February 25, 2026. The
[three-year history](lab10_nvda.md#three-year-filing-history) also traces FY2024
and FY2025 figures to their respective Forms 10-K.

Important reported FY2026 facts are revenue of $215,938, Data Center revenue of
$193,737, net income of $120,067, operating cash flow of $102,718, capital
spending of $6,042, cash of $10,605, marketable securities of $51,951, debt of
$8,468, and 24,514 million diluted weighted-average shares. These are reported
facts, not forecasts. Forecast paths, the discount rate, and terminal growth
are judgment assumptions.

The periods and definitions are not perfectly aligned. The accounting base is
FY2026, the peer comparison uses September 10, 2026 closes and the latest
annual GAAP diluted EPS available then, and the pro-forma comparison uses a
September 24, 2026 quote. The model therefore does not pretend that all inputs
come from one point in time. Later FY2027 results were public before the market
observations but were not incorporated into the saved annual base, which is a
material limitation.

### 3. Own-company pro-forma

The model forecasts FY2027–FY2031. It separates Data Center revenue from other
revenue because one consolidated growth rate would hide NVIDIA's principal
economic driver. The base Data Center growth path is 35%, 25%, 18%, 12%, and
8%; other-revenue growth is 10%, 10%, 9%, 8%, and 7%. The Data Center path is a
judgment informed by reported growth slowing from 217% to 142% to 68%, not
company guidance. Other central assumptions include a 72.5% gross margin,
R&D declining gradually from 8.5% to 8.0% of revenue, SG&A at 3.0% of gross
profit, capital spending at 3.0% of revenue, a 15.0% tax rate, and 120 inventory
days.

The statements are linked. Revenue determines gross profit; R&D, SG&A, and
depreciation determine operating income; interest and tax lead to net income;
inventory, capital spending, working capital, and debt repayment convert net
income to FCFE. Signed FCFE is:

`net income + depreciation − capital spending − change in inventory − change in other working capital − debt repayment`.

Liquidity is computed after FCFE, buybacks, dividends, and any borrowing. The
balance sheet must balance and the $40,000 liquidity floor must pass before the
valuation runs. In the executed base, revenue rises from $285,966.0 in FY2027E
to $500,475.0 in FY2031E, operating income rises from $174,398.5 to $303,302.5,
and FCFE rises from $132,886.7 to $244,585.5. Every annual balance gap is $0.0,
every liquidity check passes, and no short-term borrowing is drawn. A deliberate
broken-liquidity test produces a −$91,886.7 gap and correctly refuses valuation.

### 4. Valuation

| Method | Dated value and share basis | Method and main limitation |
|---|---:|---|
| FCFF DCF | **$60.00 per diluted share**, using FY2026 reported inputs and a Sept. 10, 2026 market comparison | Discounts five forecast FCFF amounts at 16.0% WACC with 3.0% terminal growth. Enterprise value of $1,468,752.8 plus $10,605 cash less $8,468 debt gives $1,470,889.8 of equity value; dividing by 24,514 million diluted shares gives $60.0020. Marketable securities were excluded from the bridge, conservatively adding a disclosed limitation. |
| FCFE pro-forma | **$62.97 per diluted share**, analysis dated Sept. 24, 2026 | Discounts linked equity cash flows at the 15.93% cost of equity with 3.0% terminal growth. Equity value is $1,543,651.9. Terminal value is 60.6% of total modeled equity value. The model holds diluted shares fixed and simplifies several balance-sheet accounts. |
| Peer P/E | **$370.66–$931.18 per common share**, Sept. 10, 2026 closes | Applies AMD's and Broadcom's annual GAAP diluted P/Es to NVIDIA's $4.90 annual diluted EPS. AMD has a much smaller Data Center concentration; Broadcom includes substantial infrastructure software. The two-peer $650.92 midpoint is arithmetic, not a defended fair value. |
| Market observations | **$218.36 per common share** on Sept. 10 and **$224.58 per common share** on Sept. 24, 2026 | The observations use different dates and price sources. They are comparison points, not model outputs. |

The methods disagree because they capitalize different information and
assumptions. The DCFs use a high discount rate, a fading growth path, and an
FY2026 accounting base. The peer method divides September prices by older
annual GAAP earnings and transfers whole-company multiples from companies with
different mixes and accounting effects. P/E produces equity value directly;
the FCFF DCF requires an enterprise-to-equity bridge; the FCFE model discounts
cash available to equity at the cost of equity.

The reverse FCFF DCF makes the disagreement visible. To reach the saved
$218.49 target while holding starting FCFF of $96,895.847, 16.0% WACC, 3.0%
terminal growth, $10,605 cash, $8,468 debt, and 24,514 million diluted shares
fixed, the model requires a uniform **+40.7945-percentage-point** shift. The
explicit growth rates become 75.79%, 65.79%, 58.79%, 52.79%, and 48.79%. This
is one mathematical solution, not proof of mispricing or proof of the market's
actual expectations.

### 5. Sensitivity and drivers

Lab 11 changes one independent input at a time and reruns the full linked model.
The Data Center path moves by ±5 percentage points in each forecast year. Gross
margin moves from the 72.5% base to 70.0% or 75.0%.

| Driver | Lower value/share | Base | Higher value/share | Full span |
|---|---:|---:|---:|---:|
| Data Center growth path | $54.03 | $62.97 | $73.29 | **$19.26** |
| Gross margin | $60.13 | $62.97 | $65.82 | **$5.69** |

For the higher-growth case, the causal path is: higher annual Data Center
growth → higher Data Center and total revenue → higher gross profit → higher
operating and net income, while linked R&D, SG&A, capital spending, inventory,
working capital, and tax also increase → higher FCFE → higher value. FY2031
operating income rises from $303,302.5 to $368,924.6, FY2031 FCFE rises from
$244,585.5 to $293,666.5, and value rises from $62.97 to $73.29. The model is
not simply applying the revenue change directly to value.

Over these tested ranges, Data Center growth is the larger driver. Its FY2031
operating-income span is $121,040.0 versus $24,273.0 for gross margin, and its
value span is $19.26 versus $5.69. This ranking is range-dependent: the growth
path changes in five compounding years, while margin changes by 2.5 points. The
cases are conditional scenarios, not probabilities, and the one-at-a-time
method omits interactions such as faster growth causing lower margins or
greater reinvestment.

### 6. Interpretation

The supported decision remains watch-defer. The two cash-flow methods cluster
near $60–$63, and even the tested higher Data Center-growth case reaches only
$73.29 compared with the saved $224.58 market observation. The peer method
points in the opposite direction but is too dispersed and economically mixed to
override the cash-flow evidence. Averaging the methods would conceal rather
than resolve their different assumptions.

I would reconsider initiation if a refreshed model using later reported results
and a defensible forward discount rate supported value near or above the market
price under a meaningful downside case. I would become more negative if
reported Data Center demand slowed, customer concentration weakened pricing
power, inventory or purchase-obligation provisions rose, margins deteriorated,
or reinvestment needs increased without corresponding cash flow.

The next research should address two linked uncertainties. First, refresh the
operating base with FY2027 results and test whether demand, margins,
reinvestment, and FCFE support the current growth path. Second, rebuild and
sensitize the forward cost of equity because the 15.93% estimate relies heavily
on a backward-looking 2.22 beta and was not varied in Lab 11. No refreshed model
or discount-rate sensitivity is claimed here.


### Questions received and answers

**Selection and evidence**

- **Question:** Why was NVIDIA a suitable target instead of merely a company
  with recent high growth?
  **Answer:** NVIDIA has a clearly identifiable driver—Data Center supplied
  89.7% of FY2026 revenue—along with detailed SEC evidence and a market price
  that can be compared with cash-flow and peer valuations. Its concentration
  makes the analysis decision-relevant because the same driver creates both
  upside and risk.
- **Follow-up:** Which source supports the 89.7% claim, and is it a forecast?
  **Answer:** NVIDIA's FY2026 Form 10-K reports $193,737 of Data Center revenue
  and $215,938 of total revenue. Dividing the two gives 89.7%. It is a
  calculation from reported FY2026 facts, not a forecast.

**Model and valuation**

- **Question:** How does the Data Center growth assumption reach value rather
  than stopping at revenue?
  **Answer:** Growth raises Data Center and total revenue. The linked model then
  recomputes gross profit, R&D, SG&A, depreciation, operating income, tax, net
  income, capital spending, inventory, other working capital, FCFE, and the
  discounted equity value. In the higher Lab 11 case, FY2031 FCFE increases by
  $49,081.0 and value rises by $10.32 per share.
- **Question:** Why does the pro-forma use cost of equity while the earlier DCF
  uses WACC?
  **Answer:** The pro-forma discounts FCFE, which belongs to common equity after
  debt cash flows, so it uses the 15.93% cost of equity. The earlier DCF
  discounts FCFF available to all capital providers, so it uses 16.0% WACC and
  then bridges enterprise value to equity value.
- **Question:** Why do the DCF and peer P/E methods disagree so much?
  **Answer:** The DCFs use an FY2026 base, a fading explicit growth path, and a
  high discount rate. The peer method uses older annual GAAP EPS with September
  prices and transfers multiples from two companies with materially different
  business mixes. The peer output is therefore a diagnostic comparison, not a
  basis for averaging the methods.
- **Follow-up unresolved gap:** If the discount rate is one of the least trusted
  inputs, why did Lab 11 test only operating drivers?
  **Answer:** Lab 11 deliberately isolated two operating drivers, so it did not
  establish the effect of discount-rate uncertainty. The gap is specific: run a
  cost-of-equity and terminal-growth sensitivity after rebuilding the forward
  discount rate. That work has not yet been performed.

**Sensitivity and interpretation**

- **Question:** Does Data Center growth rank first because it is inherently more
  uncertain than margin?
  **Answer:** No. It ranks first only over the tested ranges. Five annual growth
  rates move by five percentage points and compound, while margin moves by 2.5
  points. The sensitivity measures conditional impact, not uncertainty or
  probability.
- **Question:** What evidence could change the watch-defer conclusion?
  **Answer:** A refreshed, source-supported model would need to produce value
  near or above the market price under a credible downside case. Sustained Data
  Center demand, cash conversion, and margins together with a defensible lower
  cost of equity could move the decision toward initiate. Slower demand, margin
  pressure, larger provisions, or greater reinvestment could reinforce or
  worsen watch-defer.

### Calculation checked and result

As the substitute evidence check, the existing `dcf.py`, `lab08_pe.py`,
`lab10_nvda.py --break-test`, and `lab11_nvda.py` files were rerun on October 1,
2026. All exited successfully. The Lab 11 higher-growth trace changed only the
Data Center growth input, produced zero displayed balance gaps and passing
liquidity checks, and moved FY2031 FCFE from $244,585.5 to $293,666.5 and value
from $62.97 to $73.29. This supports the claimed direction and mechanism inside
the model; it does not validate the economic probability of the higher-growth
case.

### Explanation back, strength, and improvement

- **Explanation back:** The conclusion is watch-defer because the two
  internally linked cash-flow valuations remain far below the saved market
  price, while the peer P/E evidence is too heterogeneous to resolve the gap.
  The main tested operating driver is the five-year Data Center growth path.
  The biggest limitation is that the valuation begins with FY2026 information
  and combines a judgment growth path with an uncertain backward-looking
  discount rate.
- **Evidence-backed strength:** The analysis keeps reported facts separate from
  judgment, preserves units and dates, links the three statements, checks the
  accounting identity, and qualifies the sensitivity ranking by the ranges
  tested.
- **Specific improvement:** Refresh the annual base with later FY2027 reported
  information and then test cost of equity and terminal growth alongside the
  operating sensitivities. Do not claim a repaired model until those runs are
  completed and reconciled.

## Keep, revise, and investigate after review

- **Keep:** the watch-defer conclusion, the separation of Data Center from other
  revenue, the refusal to average incompatible valuation methods, and the
  range-qualified interpretation of Lab 11.
- **Revise:** describe the research priority as both operating evidence and the
  discount rate—not Data Center growth alone—because the review exposed that
  Lab 11 did not test a valuation input already identified as weak.
- **Investigate:** incorporate later FY2027 results; rebuild beta, risk-free
  rate, and equity-risk-premium support; run cost-of-equity/terminal-growth
  sensitivity; and test interactions between growth, margin, and reinvestment.
- **Effect on conclusion:** no change. The review identifies unresolved work but
  supplies no completed evidence that closes the gap between $54.03–$73.29 and
  the $224.58 saved market observation. It changes the research priority rather
  than the valuation conclusion.

## Reflection from the review

The question that most challenges the analysis is: **If the discount rate was
already identified as one of the least trusted assumptions, why was it not
included in Lab 11?** The improved understanding is that “largest tested
operating driver” is not the same as “largest overall source of valuation
uncertainty.” Data Center growth has the largest effect among the two tested
operating ranges, but cost-of-equity uncertainty remains unranked.

## AI-use and scope note

This Lab 12 review and its example questions and answers were drafted with
Codex. The underlying figures and models come from the linked
existing course files. The rerun verifies code execution and internal
reconciliation only; it does not turn judgment assumptions into facts.
