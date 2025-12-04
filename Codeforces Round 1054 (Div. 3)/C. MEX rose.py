from collections import defaultdict
for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    d = defaultdict(int)
    ans = 0
    for i in a:
        d[i] += 1
    for i in range(k):
        if i not in d:
            ans += 1
    if d[k] > ans:
        ans += d[k] - ans
    print(ans)



