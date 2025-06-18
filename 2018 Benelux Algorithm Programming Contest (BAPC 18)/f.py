import math

def targ_ach(inves, d, targ):
    prof = []
    for p, c in inves:
        cur_prof = p * d - c
        if cur_prof > 0:
            prof.append(cur_prof)
    
    return sum(prof) >= targ

n, m = map(int, input().split())
inves = []
for _ in range(n):
    p, c = map(int, input().split())
    inves.append((p, c))

l, r = 1, 2 * 10**9
ans = r

while l <= r:
    mid = (l + r) // 2
    if targ_ach(inves, mid, m):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
