from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    d = defaultdict(int)
    a = list(map(int, input().split()))

    for i in range(n):
        d[a[i]] += 1
    ans = 0
    new = (sorted(d.items(), key=lambda x: x[1]))
    for i in range(len(new)):
        ans = max(ans, new[i][1] * (len(new)-i))
    print(ans)