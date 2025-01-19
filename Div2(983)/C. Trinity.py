from bisect import bisect_left


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    ans = float('inf')

    for i in range(n-2):
        cur_sum = nums[i] + nums[i+1]
        ind_less = bisect_left(nums, cur_sum)
        ans = min(ans, n-(ind_less-i))

    print(ans)