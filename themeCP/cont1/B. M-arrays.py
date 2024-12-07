from collections import defaultdict

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    nums = list(map(int, input().split()))

    d = defaultdict(int)

    for i in nums:
        d[i] += 1
    