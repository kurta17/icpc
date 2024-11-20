n = int(input())
nums = list(map(int,input().split()))
pre_one = [0]
nums_sort = sorted(nums)
pre_two = [0]

for i in range(1,n+1):
    pre_one.append(pre_one[-1] + nums[i-1])
    pre_two.append(pre_two[-1] + nums_sort[i-1])


m = int(input())

for _ in range(m):
    t,l,r = map(int,input().split())
    if t == 1:
        print(pre_one[r] - pre_one[l-1])
    elif t == 2:
        print(pre_two[r] - pre_two[l-1])
