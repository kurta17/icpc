import collections


n,m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
visited = set()
ans = 0
direct = [[1,0],[-1,0],[0,1],[0,-1]]


for i in range(n):
    for j in range(m):
        if grid[i][j] == "." and (i,j) not in visited:
            ans += 1
            q = collections.deque()
            q.append((i,j))
            visited.add((i,j))

            while q:
                r,c = q.popleft()
                for dr,dc in direct:
                    rw, cl = r + dr, c + dc
                    if (rw in range(n) and cl in range(m) and (rw,cl) not in visited and grid[rw][cl] == "."):
                        q.append((rw,cl))
                        visited.add((rw,cl))

print(ans)

