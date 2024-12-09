from collections import defaultdict
import math

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    nums = list(map(int, input().split()))

    r = [0] * m
    ans = 0
    for i in range(n):
        r[nums[i] % m] += 1
        
    for i in range(m // 2 + 1):
        if r[i] + r[(m-i)%m] > 0:
          ans += max(abs(r[i] - r[(m-i)%m]), 1)



    print(ans)

