for _ in range(int(input())):
    n,m = map(int,input().split())
    grid = [list(map(int, input().strip())) for i in range(n)]
    ans = 0
    for i in range(min(n,m)//2):
        l = []

        for a in range(i,m-i):
            l.append(grid[i][a])

        for b in range(i + 1, n - i):
            l.append(grid[b][m - i - 1])
        
        if n - i - 1 != i:
            for c in range(m - i - 2, i - 1, -1):
                l.append(grid[n - i - 1][c])

        if m - i - 1 != i:
            for d in range(n-i-2,i,-1):
                l.append(grid[d][i])

        lay = l + l[:3]

        for k in range(len(l)):
            if lay[k:k+4] == [1, 5, 4, 3]:
                ans += 1
        
    print(ans)


        
