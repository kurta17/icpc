from collections import defaultdict


for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().strip()))
    d = defaultdict(int)
    for i in range(n):
        d[a[i]] += 1
    if max(d[0], d[1]) - n//2 <= k and d[0]//2 + d[1]//2 >= k and (k- max(d[0], d[1]) - n//2) % 2 == 0:
        print("YES")
    else:
        print("NO")