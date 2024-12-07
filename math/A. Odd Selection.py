import math

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    if n == 1:
        if nums[0] % 2 != 0:
            print("Yes")
        else:
            print("No")
    else:
        odd = 0
        for i in nums:
            if i % 2 != 0:
                odd+=1

        even = n - odd
        ans = False

        for o in range(1,odd+1,2):
            if x - o <= even and x - o >= 0:
                print("Yes")
                ans = True
                break

        if not ans:
            print("No")

    
