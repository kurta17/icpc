import math
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
low = nums[0]
high = nums[-1]

c_low = 0
c_high = 0

for i in nums:
    if i == low:
        c_low+=1
    if i == high:
        c_high+=1


if c_low == n and c_high==n:
    print(0, n*(n-1)//2)
else:
    print(high-low, c_high * c_low)