n,k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
eps = 10**(-6)

def good(x,k):
    cnt = 0
    for i in a:
        cnt += i//x
    return cnt >= k

l = 0
r = 1

while good(r,k): r *= 2

for i in range(50):
    mid = (l+r) / 2
    if good(mid,k):
        l = mid
    else:
        r = mid

print(l)