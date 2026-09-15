# Lab 07 — Asbury P/E Comparison

**Analysis date:** September 15, 2026

**Scope:** AI-assisted reproduction of the course's frozen Asbury case, with peer-policy explanations and a changed-peer check.

## DCF explanation and question

The AI reran the existing `python dcf.py` without editing it. It reproduced NVIDIA's saved **$60.0020 per diluted share** base case and **$53.01–$69.47** sensitivity range.

The saved inputs are starting free cash flow to the firm of $96,895.847 million; annual forecast growth of 35%, 25%, 18%, 12%, and 8%; weighted average cost of capital of 16%; and terminal growth of 3%. Higher forecast cash flow or terminal growth raises value; a higher discount rate lowers it. The sensitivity grid varies the discount rate from 15% to 17% and terminal growth from 2% to 4%.

The saved assumptions and sources remain in [Lab 06](lab06_nvda.md). This reopening check adds no new NVIDIA research. Asbury's share price and NVIDIA's DCF describe different companies, so their dollar values do not form a valuation comparison.

**Question investigated:** Why can two companies with similar business activities trade at different P/E multiples, and when is it reasonable to apply one company's multiple to another company's earnings?

## What P/E measures

Price-to-earnings (P/E) = market price per share / annual diluted earnings per share (EPS).

Price is what investors pay for one share. Diluted EPS is reported profit attributable to common shareholders per weighted-average diluted share, allowing for potential dilution under the accounting rules. A 10x P/E means investors pay $10 of share price for $1 of annual earnings per share. It is not a guaranteed ten-year payback.

Dividing by earnings puts differently sized companies on a common basis. Comparable-company valuation asks what Asbury's shares would be worth if investors priced its earnings like the peers' earnings. A discounted cash flow (DCF) valuation instead uses a forecast of future cash flows.

Useful peers need similar business economics, growth, risk, and financing characteristics. Prices need the same trading date, and EPS needs compatible periods, accounting definitions, currency, share basis, and split treatment. Negative or zero EPS makes this positive P/E valuation not meaningful. Unusual profits can make P/E look artificially low; depressed earnings can make it look high. Lower P/E can reflect weaker growth or greater risk rather than a bargain.

## Peer decisions and business evidence

The following AI-assisted peer policy follows the course's worked case and uses business fit as the basis for inclusion.

| Candidate | Decision | Business reason and difference |
|---|---|---|
| AutoNation (AN) | Use, with its finance business noted | Like Asbury, it sells new/used vehicles and provides parts/service and finance/insurance activities. AutoNation Finance is a difference to examine because lending can change earnings and risk. |
| Group 1 (GPI) | Qualify and include for the worked calculation | It shares the franchised vehicle-retail and parts/service model, but operates in both the U.S. and U.K. Its 2024 acquisition of 54 Inchcape dealerships changes the business being compared. Geography and acquisition effects need to remain visible. |

Franchised dealerships and service/parts explain how the firms earn money better than a broad automotive industry label. A manufacturer or a different retail model would not automatically qualify. Qualification here means naming the difference and testing its consequence; it does not apply an arbitrary discount.

Business evidence: [course worked case, “Read the business evidence first”](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-04/teach-comps-worked-example.md#read-the-business-evidence-first).

## Frozen inputs and checked calculation

All inputs below are **course-provided**, in U.S. dollars per share. Prices are December 31, 2024 closes; EPS is FY2024 **total GAAP diluted EPS**, including discontinued operations where applicable, not adjusted or continuing-operations-only EPS.

| Company | Role | Price | EPS |
|---|---|---:|---:|
| Asbury (ABG) | Target, excluded from peer median | $243.03 | $21.50 |
| AutoNation (AN) | Peer | $169.84 | $16.92 |
| Group 1 (GPI) | Qualified peer | $421.48 | $36.81 |

This is retrospective training: annual earnings were released after the price date. It is not a tradeable point-in-time signal or current market valuation.

Execution command:

```powershell
python lab07_pe.py
```

| Check | Executed result | Matches lab |
|---|---:|---|
| AN P/E | 10.037825x | Yes |
| GPI P/E | 11.450149x | Yes |
| Peer median P/E | 10.743987x | Yes |
| Asbury implied range | $215.81–$246.18 | Yes |
| Asbury at peer median | $231.00 | Yes |
| Remove GPI: AN reference estimate | $215.81 | Yes |
| Change from full-peer estimate | −$15.18/share | Yes |

## Calculation check and explanation

**AI-assisted worked calculation:** AutoNation's multiple is `169.84 / 16.92 = 10.037825059...`. Applying that unrounded multiple to Asbury's annual EPS gives `(169.84 / 16.92) * 21.50 = 215.813238770...`, displayed as **$215.81 per share**. This asks what Asbury's share price would be if its earnings received AutoNation's P/E.

For two peers, the median is their average multiple. The target-implied price uses Asbury's EPS. The program uses unrounded values internally and rounds only printed multiples and prices. P/E already produces an equity price, so no cash/debt bridge is applied.

## Changed-peer result and interpretation

**Expected direction from the model:** Removing the higher-multiple GPI should lower the median-implied price. With only AN remaining, the two-peer range should become one reference estimate.

Removing GPI removes the higher P/E, leaving AN's lower multiple. The estimate falls from the unrounded two-peer midpoint to AN's reference estimate: **−$15.18/share**. Subtracting the printed $215.81 and $231.00 gives −$15.19 because both displayed prices were already rounded; the required change uses unrounded values.

One peer gives one reference estimate, with no peer-implied range. Removing AN instead leaves GPI's **$246.18** reference estimate, a **+$15.18/share** change. Neither scenario is a reason to change the original peer policy merely to obtain a preferred price.

The $243.03 observed Asbury price is inside the two-peer range. This does not prove fair value: the result depends on only two peers, reported earnings, and differences in growth, geography, acquisitions, and financing. The range is not a confidence interval or an investment recommendation.

## Verification, sources, and AI use

- AI executed the calculator and saved its output in [outputs/lab07_output.txt](outputs/lab07_output.txt).
- An independent standard-library Decimal calculation matched all seven supplied checks. Additional executed checks passed for both removals, one/no valid peers, duplicate tickers, target exclusion, and missing, nonpositive, nonnumeric, or nonfinite price/EPS inputs. Invalid target price disables its observed P/E; valid target EPS still supports peer-implied prices.
- The calculator does not fetch data or require installed packages. Source reading was separate from calculation. The AI read the public course case; it did not independently reverify all six underlying price/EPS disclosures.
- Requirements: [Lab 07](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-04/lab-07-comparable-policy.md). Definitions: [Week 4 handout](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-04/student-handout.md). The [worked case](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-04/teach-comps-worked-example.md#a-frozen-historical-comparison) links the primary disclosures and exact locators.
- AI attribution: Codex assisted in writing the report and calculator and performed the terminal execution and numerical checks. The peer policy and explanations are AI-assisted analysis based on the course case.
