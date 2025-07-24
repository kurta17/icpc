t = input()
p = input()
a = list(map(int, input().split()))
ar = [0] * len(t)

for i in range(len(t)):
    ar[i] = a[i] - 1

def ispossible(mid,p,t,ar):
    hs = set(ar[:mid])
    p2 = 0
    for i in range(len(t)):
        if i not in hs:
            if p2 < len(p) and t[i] == p[p2]:
                p2 += 1
    return p2 == len(p)

l = 0
r = len(t)

while r>l+1:
    mid = (l+r) // 2
    if ispossible(mid,p,t,ar):
        l = mid
    else:
        r = mid

print(l)