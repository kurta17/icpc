def minimum_sort_cost(n, s):
    # Check if array is already sorted
    if all(s[i] <= s[i + 1] for i in range(n - 1)):
        return 0

    # Precompute sorted prefix lengths
    sorted_prefix = [0] * n
    sorted_prefix[0] = 1
    for i in range(1, n):
        if s[i] >= s[i - 1]:
            sorted_prefix[i] = sorted_prefix[i - 1] + 1
        else:
            sorted_prefix[i] = 1

    # Precompute sorted suffix lengths
    sorted_suffix = [0] * n
    sorted_suffix[n - 1] = 1
    for i in range(n - 2, -1, -1):
        if s[i] <= s[i + 1]:
            sorted_suffix[i] = sorted_suffix[i + 1] + 1
        else:
            sorted_suffix[i] = 1

    # Try all valid combinations of prefix and suffix sorts
    min_cost = float('inf')
    for p in range(1, n + 1):  # Prefix sort of length p
        for s in range(1, n + 1):  # Suffix sort of length s
            if sorted_prefix[p - 1] + sorted_suffix[n - s] >= n:
                # Full array can be sorted
                cost = p * p + s * s
                min_cost = min(min_cost, cost)

    return min_cost

# Input reading
n = int(input())
s = list(map(int, input().split()))

# Solve and output result
print(minimum_sort_cost(n, s))
# 