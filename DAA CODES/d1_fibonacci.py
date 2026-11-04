# DAA-1 : Fibonacci numbers - non-recursive (iterative) and recursive, with time/space analysis
import time

calls = 0


def fib_iterative(n):
    """Time O(n), Space O(1)"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n):
    """Time O(2^n), Space O(n) (depth of recursion stack)"""
    global calls
    calls += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == "__main__":
    try:
        n = int(input("Enter n : "))
    except ValueError:
        raise SystemExit("Please enter a whole number.")
    if n < 0:
        raise SystemExit("n must be 0 or more.")

    print(f"\nFibonacci series (first {n} terms): ", end="")
    print(*[fib_iterative(i) for i in range(n)])
    print(f"\n{'n':>4} {'fib(n)':>10} {'iter time(s)':>14} {'recur time(s)':>15} {'recursive calls':>16}")
    for k in (5, 10, 15, 20, 25, 30):
        t1 = time.perf_counter(); r1 = fib_iterative(k); t1 = time.perf_counter() - t1
        calls = 0
        t2 = time.perf_counter(); r2 = fib_recursive(k); t2 = time.perf_counter() - t2
        assert r1 == r2
        print(f"{k:>4} {r1:>10} {t1:>14.7f} {t2:>15.7f} {calls:>16}")
    print("\nComplexity:")
    print("  Iterative : Time O(n)    , Space O(1)")
    print("  Recursive : Time O(2^n)  , Space O(n)  (call stack)")
