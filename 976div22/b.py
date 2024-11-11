import math

t = int(input())

for _ in range(t):
    k = int(input())
    l, r = 1, (10**18) * 2
    while l < r:
        mid = (l + r) // 2
        off =int(math.isqrt(mid))

        on = mid - off
        
        if on < k:
            l = mid + 1
        else:
            r = mid
    print(l)