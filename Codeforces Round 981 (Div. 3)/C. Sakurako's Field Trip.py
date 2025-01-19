import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(1,n//2):
        if nums[i] == nums[i-1] or nums[n-i] == nums[n-i-1]:
            nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
        
    ans = 0
    
    for i in range(1,n):
        if nums[i] == nums[i-1]:
            ans += 1
    
    print(ans)