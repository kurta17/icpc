for _ in range(int(input())):
    n = int(input())
    maps = [list(map(str,input().strip())) for i in range(n)]
    ans = []

    for k in range(n-1,-1,-1):
        for i in range(4):
            if maps[k][i] == '#':
                ans.append(i+1)
                break
    print(*ans)