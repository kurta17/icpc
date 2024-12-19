t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    i = nums[0]
    j = 0

    for ind in range(1,n):
        if nums[ind] % i != 0:
            j = nums[ind]
            break

    ans = True
    
    for ind in range(2,n):
        if nums[ind] % i == 0 or nums[ind] % j == 0:
            ans = True
        else:
            ans = False
            break

    print("YES") if ans else  print("NO")
    
