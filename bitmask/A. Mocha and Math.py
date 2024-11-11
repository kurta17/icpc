t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    ans = nums[0]

    for i in range(1,n):
        ans &= nums[i]
    print(ans)
