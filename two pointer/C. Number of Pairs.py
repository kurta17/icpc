from bisect import bisect_left, bisect_right

t = int(input())

for _ in range(t):
    n,l,r = map(int, input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    if len(nums) == 1:
        print(0)
    else:
        ans = 0
        for i in range(n):
            left = bisect_left(nums, l - nums[i], i + 1)
            right = bisect_right(nums, r - nums[i], i + 1)
            ans += right - left
        print(ans)

