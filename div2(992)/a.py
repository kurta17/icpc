from collections import defaultdict
import math

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(n):
        found = False
        for j in range(n):
            if j != i:
                if abs(nums[i] - nums[j]) % k == 0:
                    found = True

        if not found:
            print("YES")
            print(i+1)
            break
    else:
        print("NO")
