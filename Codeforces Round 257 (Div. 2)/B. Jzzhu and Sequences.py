import math

nums = list(map(int, input().split()))
n = int(input())
mod = 10**9 +7
nums.append(nums[1]-nums[0])
i = (n-1) % 3

if math.ceil(n / 3) % 2 != 0:
    print(nums[i]%mod)
else:
    print(-nums[i]%mod)
