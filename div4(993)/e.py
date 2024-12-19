import math
t = int(input())

for _ in range(t):
    k,l1,r1,l2,r2 = map(int, input().split())
    count = 0
    kk = 1

    while kk <= r2:
        low = max(l1, (l2 + kk - 1) // kk)
        high = min(r1, r2 // kk)

        if low <= high:
            count += high - low + 1
        
        if kk > r2 // k:
            break
        kk *= k

    print(count)
