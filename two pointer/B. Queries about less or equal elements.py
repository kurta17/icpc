n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
ans = []

for bj in b:
    l = 0
    r = n
    while l < r:
        m = (l+r)//2
        if a[m] <= bj:
            l = m+1
        else:
            r = m
    ans.append(l)

print(*ans)