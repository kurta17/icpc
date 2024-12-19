t = int(input())

for _ in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        row = list(map(str, input().strip()))
        grid.append(row)
    
    ans = 0
    ans = 0
    for i in range(n // 2):
        for j in range(n // 2):
            M = [grid[i][j], grid[n - 1 - j][i], grid[n - 1 - i][n - 1 - j], grid[j][n - 1 - i]]
            c = max(M)
            for e in M:
                ans += ord(c) - ord(e)
    
        
    print(ans)