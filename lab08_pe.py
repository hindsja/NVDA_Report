"""Lab 08: NVIDIA peer P/E using the Lab 07 calculator's input checks.

Run from this folder: python lab08_pe.py
"""

from math import isfinite
from statistics import median


# USD/common share. September 10, 2026 unadjusted closes; latest annual
# reported GAAP total diluted EPS public by that date. See lab08_nvda.md.
TARGET = {"ticker": "NVDA", "price": 218.36, "eps": 4.90}
PEERS = [
    {"ticker": "AMD", "price": 503.60, "eps": 2.65},
    {"ticker": "AVGO", "price": 360.83, "eps": 4.77},
]


# These input checks are carried forward from the Lab 07 calculator.
def positive_number(value):
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and isfinite(value)
        and value > 0
    )


def ticker(company):
    return str(company.get("ticker") or "").strip().upper()


def pe(company):
    price, eps = company.get("price"), company.get("eps")
    if not positive_number(price) or not positive_number(eps):
        return None
    return price / eps


def main(target=TARGET, peers=PEERS):
    print("Lab 08 - NVIDIA peer P/E comparison")
    print("Prices: September 10, 2026 closes, USD/common share.")
    print("EPS: latest annual reported GAAP total diluted EPS public by that date.")

    target_symbol = ticker(target)
    target_eps = target.get("eps")
    target_multiple = pe(target)
    print(f"Target inputs: {target}")
    print(
        f"Target observed P/E: {target_multiple:.6f}x (not in peer median)"
        if target_multiple is not None else
        "Target observed P/E: not meaningful (invalid price or EPS)."
    )

    seen = set()
    multiples = []
    for company in peers:
        symbol = ticker(company)
        if not symbol or symbol == target_symbol or symbol in seen:
            print(f"Skipped peer {symbol or '<missing>'}: blank, target, or duplicate.")
            continue
        seen.add(symbol)
        multiple = pe(company)
        print(f"Peer inputs: {company}")
        if multiple is None:
            print(f"{symbol} P/E: not meaningful (invalid price or EPS).")
        else:
            multiples.append((symbol, multiple))
            print(f"{symbol} P/E: {multiple:.6f}x")

    if not positive_number(target_eps):
        print("No implied NVIDIA price: invalid target EPS.")
        return
    if not multiples:
        print("No usable peers; no implied NVIDIA price.")
        return

    prices = [(symbol, multiple * target_eps) for symbol, multiple in multiples]
    midpoint = median(value for _, value in prices)
    print(f"Peer median P/E: {median(value for _, value in multiples):.6f}x")
    if len(prices) == 1:
        print(f"One-peer NVIDIA reference: ${midpoint:.2f}/share; no range.")
    else:
        print(f"NVIDIA implied range: ${min(value for _, value in prices):.2f}-"
              f"${max(value for _, value in prices):.2f}/share")
        print(f"NVIDIA peer-median estimate: ${midpoint:.2f}/share")

    print("Leave-one-peer-out (change from full-peer median estimate)")
    for removed, _ in multiples:
        remaining = [value for symbol, value in prices if symbol != removed]
        if not remaining:
            print(f"Remove {removed}: no estimate; no peers remain.")
        else:
            estimate = median(remaining)
            label = "reference; no range" if len(remaining) == 1 else "median estimate"
            print(f"Remove {removed}: ${estimate:.2f}; "
                  f"change {estimate - midpoint:+.2f} USD/share; {label}.")
    print("P/E implies a common-equity share price directly; no net-debt bridge.")


if __name__ == "__main__":
    main()
