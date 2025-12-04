n = int(input())
m = list(map(int, input().split()))
m.sort()
ss = sum(m)
dp = [False] * (ss+1)
dp[0] = True

for coin in m:
    for i in range(ss,coin-1,-1):
        if dp[i-coin]:
            dp[i] = True
ans = []
for i in range(1,ss+1):
    if dp[i]:
        ans.append(i)
print(len(ans))
print(*ans)
       