# Lab 09 — ABG Three-Statement Pro-Forma

**Question:** What are five years of a company's statements worth, built from assumptions that can be defended, and how do we know the statements are right?

**Case:** Asbury Automotive Group (ABG), FY2026E–FY2030E. Monetary amounts are USD millions unless stated otherwise. The model is implemented in [`proforma.py`](proforma.py).

## Assumption set

The following inputs are supplied by the Lab 09 instructions. They are not independently estimated in this submission.

| Assumption | ABG value | Label |
|---|---:|---|
| Organic revenue growth | 1.8% a year | Judgment |
| Gross margin | 17.05% | Judgment |
| SG&A / gross profit, 2026–2030 | 66.5%, 65.5%, 64.5%, 64.5%, 64.5% | Judgment |
| Depreciation / opening PP&E | 82.4 / 3,070.4 | History |
| Non-cash impairment | 120 a year | Judgment |
| Capital spending | 250 a year | Guidance |
| Tax rate | 25.5% | Judgment |
| Inventory days | 2,135.8 / (17,999.0 − 3,071.7) × 365 | History |
| Floor plan / inventory | 2,027.0 / 2,135.8 | History |
| Other working capital | 0.8% of change in revenue | Judgment |
| Minimum cash / revolver limit / revolver rate | 25 / 850 / 6% | History / judgment / judgment |
| Debt repayment / share buyback | 150 / 150 a year | Judgment |
| Floor plan / term debt interest | 4.67% / 5.44% | History |
| Cost of equity / terminal growth | 10% / 2.5% | Judgment |
| Shares outstanding | 17.951349 million | Fact supplied from June 30, 2026 10-Q |

The supplied FY2025 opening balance sheet is revenue 17,999.0; inventory 2,135.8; PP&E 3,070.4; other assets 6,371.6; cash 40.4; floor plan 2,027.0; term debt 3,572.0; other liabilities 2,127.5; and equity 3,891.7.

## Engine and known-answer proof

The engine calculates the income statement first, then all balance-sheet accounts except cash, then free cash flow to equity (FCFE), and finally cash. Interest is based on opening financing balances. A revolver draw occurs only if cash would otherwise fall below 25; excess cash repays an opening revolver first. The balance-sheet identity and minimum-cash condition must pass before valuation runs.

Executed with `python proforma.py`:

| Line | FY2026E | FY2030E | Lab target | Result |
|---|---:|---:|---:|---|
| Revenue | 18,323.0 | 19,678.3 | 18,323.0 / 19,678.3 | Match |
| Operating income | 844.2 | 971.4 | 844.2 / 971.4 | Match |
| Net income | 413.6 | 527.5 | 413.6 / 527.5 | Match |
| Free cash flow to equity | 211.4 | 342.3 | 211.4 / 342.3 | Match |
| Cash, year end | 101.8 | 719.8 | 101.8 / 719.8 | Match |
| Assets − liabilities − equity | 0.0 | 0.0 | 0.0 / 0.0 | Match |

The discounted equity value is **$5,237.34 million**, or **$291.75 per share**. The discounted terminal value is **79.8%** of total equity value, so most of the valuation depends on cash flows after the explicit forecast. The result is therefore especially sensitive to the 10% cost of equity, 2.5% terminal growth, and the normalized terminal FCFE.

## Why cash is computed last

Cash is the residual result of the operating, investing, and financing decisions. Revenue and margins determine earnings; inventory, floor plan borrowing, capital spending, impairments, debt repayment, and buybacks determine the cash movements. Computing cash before those linked accounts would hide missing or double-counted flows. Computing it last makes the ending cash balance an auditable consequence of the whole model.

The rejection test makes this control visible. Replacing FY2026E computed cash of 101.8 with opening cash of 40.4 lowers assets by 61.4 without changing liabilities or equity. The assertion must refuse valuation and report:

```text
FY2026E balance check failed: assets - liabilities - equity = -61.4
```

The **−61.4** identifies both direction and size: assets are short by the unrecorded FY2026 cash increase. It points to the cash roll-forward before any individual formula is opened.

## Floor plan financing

A floor plan is short-term inventory financing supplied by manufacturers' finance affiliates or banks. In this case, the projected balance moves with inventory, interest is charged on the opening floor plan balance, and the change in floor plan is included in FCFE as an operating financing inflow or outflow. Removing that line would keep the inventory cash outflows but eliminate their linked financing; over the model horizon, that mismatch can drive cash deeply negative (about negative $1.1 billion in the course video).

