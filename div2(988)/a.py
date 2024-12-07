from collections import defaultdict
import math

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    d = defaultdict(int)

    for i in nums:
        d[i] += 1

    ans = 0

    for j in d:
        ans += math.floor(d[j]/2) 
        
    print(ans)