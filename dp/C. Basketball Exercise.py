n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0] * (n) for i in range(3)]
dp[0][0] = a[0]
dp[1][0] = b[0]
dp[2][0] = 0

for i in range(1,n):
    dp[0][i] = a[i] + max(dp[1][i-1] , dp[2][i-1])
    dp[1][i] = b[i] + max(dp[0][i-1] , dp[2][i-1])
    dp[2][i] = max(dp[0][i-1],dp[1][i-1])
                          
print(max(dp[0][-1],dp[1][-1],dp[2][-1]))