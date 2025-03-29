import math

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    curr = 0
    
    for i in range(n-1,-1,-1):
        if a[i] >= x:
            ans += 1
        else:
            curr += 1
            if a[i] * (curr)  >= x:
                ans += 1
                curr = 0

    print(ans)
