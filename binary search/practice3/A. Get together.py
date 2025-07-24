n = int(input())
xi = []
v = []
for _ in range(n):
    x_i, v_i = map(int, input().split())
    xi.append(x_i)
    v.append(v_i)

def can_meet(xi,v,t):
    l = -float('inf')
    r = float('inf')

    for i in range(n):
        l = max(l, xi[i] - v[i]*t)
        r = min(r, xi[i] + v[i]*t)
    
    return l <= r

max_s = max(xi)
min_s = min(xi)
min_v = min(v)
dist = max_s - min_s

l = 0
r = (max_s - min_s)/min_v

for i in range(100):
    mid = (l+r)/2
    if can_meet(xi,v,mid):
        r = mid
    else:
        l = mid

print(l)