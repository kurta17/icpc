from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    cord = list(map(int, input().split()))

    c = defaultdict(int)

    for i in cord:
        c[i] += 1


    ans = []

    for i,v  in c.items():
        ans.extend([i]*(v//2))

    ans.sort()

    if len(ans) < 4:
        print("NO") 
    else:
        print("YES")
        print(ans[0],ans[1],ans[0], ans[-1], ans[-2], ans[1], ans[-2], ans[-1])   