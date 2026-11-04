# DAA-3 : Fractional knapsack using greedy method (highest value/weight ratio first)

def fractional_knapsack(values, weights, capacity):
    items = sorted(zip(range(1, len(values) + 1), values, weights),
                   key=lambda x: x[1] / x[2], reverse=True)
    total, remaining = 0.0, capacity
    print(f"{'Item':<5}{'Value':<7}{'Weight':<8}{'Ratio':<8}{'Taken':<10}")
    for no, v, w in items:
        if remaining == 0:
            break
        take = min(w, remaining)
        total += v * take / w
        remaining -= take
        print(f"{no:<5}{v:<7}{w:<8}{v / w:<8.2f}{take}/{w}")
    return total


if __name__ == "__main__":
    try:
        n = int(input("Enter number of items : "))
        values = [int(x) for x in input("Enter values  : ").split()]
        weights = [int(x) for x in input("Enter weights : ").split()]
        cap = int(input("Enter knapsack capacity : "))
    except ValueError:
        raise SystemExit("Invalid input: please enter whole numbers only.")
    # FIX: validate input (a weight of 0 caused ZeroDivisionError)
    if n <= 0 or len(values) != n or len(weights) != n:
        raise SystemExit("Invalid input: enter exactly n values and n weights.")
    if cap < 0 or any(w <= 0 for w in weights) or any(v < 0 for v in values):
        raise SystemExit("Invalid input: weights must be positive; values and capacity non-negative.")
    print()
    best = fractional_knapsack(values, weights, cap)
    print(f"\nMaximum value in knapsack = {best:.2f}")
    print("Time complexity: O(n log n) (sorting)")
