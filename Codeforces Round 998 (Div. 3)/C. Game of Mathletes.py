from collections import defaultdict


for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    l, r = 0, n - 1
    score = 0

    while l < r:
        s = a[l] + a[r]
        if s == k:
            score += 1
            l += 1
            r -= 1
        elif s < k:
            l += 1
        else:
            r -= 1

    print(score)