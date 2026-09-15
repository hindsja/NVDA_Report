"""Lab 07: frozen Asbury P/E comparison. Run: python lab07_pe.py"""

# Editable inputs: USD per share; FY2024 total GAAP diluted EPS.
# Prices are December 31, 2024 closes; EPS was reported afterward.
TARGET = {"ticker": "ABG", "price": 243.03, "eps": 21.50}
PEERS = [
    {"ticker": "AN", "price": 169.84, "eps": 16.92},
    {"ticker": "GPI", "price": 421.48, "eps": 36.81},
]

from math import isfinite
from statistics import median


def positive_number(value):
    """Reject missing, nonnumeric, nonfinite, zero, and negative inputs."""
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
    print("Lab 07 - Asbury comparable-company P/E")
    print("USD/share; December 31, 2024 prices; FY2024 total GAAP diluted EPS.")
    print("Retrospective training case: annual earnings were reported afterward.")
    print(f"Target inputs: {target}")
    target_pe = pe(target)
    if target_pe is None:
        print("Target observed P/E: not meaningful (invalid price or EPS).")
    else:
        print(f"Target observed P/E: {target_pe:.6f}x (excluded from peer median)")

    # Keep the first occurrence of each ticker, ignoring case and whitespace.
    unique_peers = []
    seen = set()
    for company in peers:
        symbol = ticker(company)
        if not symbol:
            print("Peer skipped: missing ticker.")
        elif symbol == ticker(target):
            print(f"{symbol} skipped: target cannot be its own peer.")
        elif symbol in seen:
            print(f"{symbol} skipped: duplicate ticker (first occurrence retained).")
        else:
            seen.add(symbol)
            unique_peers.append((symbol, pe(company)))
            print(f"Peer inputs: {company}")

    print("\nPeer multiples")
    for symbol, multiple in unique_peers:
        if multiple is None:
            print(f"{symbol} P/E: not meaningful (invalid price or EPS).")
        else:
            print(f"{symbol} P/E: {multiple:.6f}x")

    valid_multiples = [value for _, value in unique_peers if value is not None]
    target_eps = target.get("eps")
    full_estimate = None
    if not valid_multiples:
        print("\nNo usable peers; no implied-price estimate.")
    else:
        midpoint = median(valid_multiples)
        print(f"\nPeer median P/E: {midpoint:.6f}x")
        if not positive_number(target_eps):
            print("Target implied prices: not meaningful (invalid target EPS).")
        elif len(valid_multiples) == 1:
            full_estimate = midpoint * target_eps
            print(f"One valid peer: reference estimate ${full_estimate:.2f}; no range.")
        else:
            # Round only for display, never before valuation or subtraction.
            low = min(valid_multiples) * target_eps
            full_estimate = midpoint * target_eps
            high = max(valid_multiples) * target_eps
            print(f"Minimum-multiple implied price: ${low:.2f}")
            print(f"Median-multiple implied price: ${full_estimate:.2f}")
            print(f"Maximum-multiple implied price: ${high:.2f}")
            print(f"Peer-implied range: ${low:.2f}-${high:.2f}")

    print("\nLeave-one-peer-out (change from full-peer median estimate)")
    for removed_symbol, _ in unique_peers:
        remaining = [
            value for symbol, value in unique_peers
            if symbol != removed_symbol and value is not None
        ]
        if not remaining:
            print(f"Remove {removed_symbol}: no usable peers remain; no estimate.")
        elif not positive_number(target_eps):
            print(f"Remove {removed_symbol}: implied price not meaningful (invalid target EPS).")
        else:
            estimate = median(remaining) * target_eps
            change = estimate - full_estimate
            label = "reference estimate; no range" if len(remaining) == 1 else "median estimate"
            print(
                f"Remove {removed_symbol}: ${estimate:.2f}; "
                f"change {change:+.2f} USD/share; {label}."
            )
    print("\nP/E implies an equity price directly; no cash/debt bridge.")


if __name__ == "__main__":
    main()
