n,d = map(int,input().split())
a = list(map(int,input().split()))

t = n
a.sort(reverse=True)
i = 0
ans = 0

while t > 0:
    memb = d // a[i] + 1
    t -= memb
    if t >= 0:
        ans += 1
    i += 1

print(ans)

