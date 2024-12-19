import math
t = int(input())


for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    s = sum(nums)

    pref = 0
    ans = 0

    for i in range(n-1):
        pref += nums[i]
        ans = max(ans, math.gcd(pref, s-pref))

    print(ans)
