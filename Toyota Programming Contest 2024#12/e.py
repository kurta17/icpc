
n = int(input())
a = list(map(int, input().split()))
b =  list(map(int, input().split()))
dp = [[0] * n] * n
for i in range(n):
    for j in range(n):
        dp[i][j] = abs(a[i] - b[j])

k  = int(input())
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(dp[x][y])