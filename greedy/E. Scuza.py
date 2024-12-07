import bisect
t = int(input())

for _ in range(t):
    n,q = map(int, input().split())
    st = list(map(int,input().split()))
    l = list(map(int,input().split()))

    ans = []
    pre = [st[0]]

    for i in range(1,n):
        pre.append(pre[i-1]+st[i])

    pre_max = [st[0]]

    for i in range(1,n):
        pre_max.append(max(pre_max[i-1],st[i]))

    for i in range(q):
        ind = bisect.bisect_right(pre_max,l[i])
        if ind == 0:
            ans.append(0)
        
        else:
            ans.append(pre[ind-1])
    print(*ans)
    