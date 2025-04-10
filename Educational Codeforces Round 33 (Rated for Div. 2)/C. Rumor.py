from collections import defaultdict


n, m = map(int, input().split())
coins = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(st,visited):
    stack = [st]
    mc = float('inf')
    while stack:
        node = stack.pop()

        if not visited[node-1]:
            visited[node-1] = True
            mc = min(mc, coins[node-1])

            for neigh in graph[node]:
                if not visited[neigh-1]:
                    stack.append(neigh)
    return mc

visited = [False] * n
ans = 0

for i in range(1,n+1):
    if not visited[i-1]:
        c = dfs(i,visited)
        ans += c

print(ans)
