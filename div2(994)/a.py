
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    if set(nums) == {0}:
        print(0)
    else:
        diff = 0
        if nums[0] != 0:
            diff += 1
        for i in range(1,n):
            if (nums[i-1] == 0 and nums[i] != 0):
                diff += 1
        if diff <= 1:
            print(1)
        else:
            print(2)
                
        