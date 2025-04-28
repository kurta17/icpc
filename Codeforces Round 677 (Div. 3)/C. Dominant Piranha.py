for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dom = float('-inf')
    ans = 0
    if a[0] > a[1]:
        dom = a[0] + 1
        ans = 1

    for i in range(1,n-1):
        if a[i] > a[i-1] or a[i] > a[i+1]:
            if dom < a[i]+1:
                dom = a[i] + 1
                ans = i+1

    if a[-2] < a[-1]:
        if dom < a[-1] + 1:
            dom = a[-1] + 1
            ans = n
        

    if dom == float('-inf') or len(set(a)) == 1:
        print(-1)
    else:
        print(ans)