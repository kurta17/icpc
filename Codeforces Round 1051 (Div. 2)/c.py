from collections import deque

for _ in range(int(input())):
    n = int(input())
    g = [[] for _ in range(n)]
    d = [0] * n

    for _ in range(n-1):
        u,v,x,y = map(int, input().split())
        u -= 1
        v -= 1
        if x>y:
            g[v].append(u)
            d[u] += 1
        else:
            g[u].append(v)
            d[v]+=1

    q = deque()

    for i in range(n):
        if d[i] == 0:
            q.append(i)

    o = []
    while q:
        f = q.popleft()
        o.append(f)
        for v in g[f]:
            d[v] -= 1
            if d[v] == 0:
                q.append(v)
    ans = [0] * n

    for i in range(n):
        ans[o[i]] = i+1
    print(*ans)