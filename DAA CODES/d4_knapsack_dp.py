# DAA-4 : 0-1 Knapsack using dynamic programming

def knapsack_01(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]                       # do not take item i
            if weights[i - 1] <= w:                       # take item i
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
    # find which items were selected
    chosen, w = [], W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i)
            w -= weights[i - 1]
    return dp, sorted(chosen)


if __name__ == "__main__":
    try:
        n = int(input("Enter number of items : "))
        values = [int(x) for x in input("Enter values  : ").split()]
        weights = [int(x) for x in input("Enter weights : ").split()]
        W = int(input("Enter knapsack capacity : "))
    except ValueError:
        raise SystemExit("Invalid input: please enter whole numbers only.")
    # FIX: validate input
    if n <= 0 or len(values) != n or len(weights) != n:
        raise SystemExit("Invalid input: enter exactly n values and n weights.")
    if W < 0 or any(v < 0 for v in values) or any(w <= 0 for w in weights):
        raise SystemExit("Invalid input: weights must be positive; values and capacity non-negative.")
    dp, chosen = knapsack_01(values, weights, W)
    print("\nDP table (rows = items 0..n, columns = capacity 0..W):")
    for row in dp:
        print(" ".join(f"{x:>4}" for x in row))
    print(f"\nMaximum value = {dp[n][W]}")
    print("Items selected (1-based):", chosen)
    print("Time complexity: O(n*W), Space: O(n*W)")
