from collections import defaultdict
import math

t = int(input())

for _ in range(t):
    k = int(input())
    nums = list(map(int, input().split()))
    s = set()
    el = k - 2

    for n in nums:
        if el % n == 0:
            m = el // n
            if m in s:
                print(n,m)
                break
            s.add(n)
