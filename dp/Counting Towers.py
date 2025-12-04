dp = [0] * (10**6 + 1)
dp[1] = 2
dp[2] = 8

for i in range(3,7):
    dp[i] = 4*dp[i-1] + dp[i-2]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])