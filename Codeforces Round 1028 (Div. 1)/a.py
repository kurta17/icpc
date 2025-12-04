import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    g = a[0]
    for i in range(1,n):
        g = math.gcd(g,a[i])
    if g in a:
        print(n - a.count(g))
        continue
    f = [float('inf')] * (mx+1)

    for j in a:
        f[j] = 0

    for x in range(mx,0,-1):
        for j in a:
            pair = math.gcd(j,x)
            # print(pair)
            f[pair] = min(f[pair], f[x] + 1)
    print(f[g] + n - 1)