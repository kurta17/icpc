n = 2 * 10**5 + 10
dp = [0] * (n)

dp[0] = 0
dp[1] = 1

for i in range(1,n):
    dp[i] = dp[i//3] + 1
    

prefix_sum = [0] * (n)

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + dp[i]

for _ in range(int(input())):
    l,r = map(int,input().split())
    print(prefix_sum[r] - prefix_sum[l-1] + dp[l])