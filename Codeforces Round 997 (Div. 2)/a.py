# from collections import defaultdict
# from functools import cmp_to_key

# for _ in range(int(input())):
#     n = int(input())
#     g = [input().strip() for _ in range(n)]
#     d = defaultdict(int)
#     for i in range(n):
#         # Count the number of '1's in the string (do not split)
#         d[i+1] = g[i].count('1')
    
#     # Define a custom comparator that uses the graph information
#     def compare(x, y):
#         # x and y are vertex labels (1-indexed)
#         # If there is an edge from x to y, then x should come before y.
#         if g[x-1][y-1] == '1':
#             return -1
#         else:
#             return 1

#     # Sort the vertices using the custom comparator
#     sorted_vertices = sorted(d.keys(), key=cmp_to_key(compare))
#     print(*sorted_vertices)

def fib(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]

    return (dp[n])
print(fib(1))