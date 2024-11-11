n = int(input())
a = list(map(int,input().split()))
dp = [-1] * n
dp[0] = a[0]
for i in range(1,n):
    if a[i] == 0:
        dp[i] = 0
    else:
        if a[i] == 1 and dp[i-1] == 1:
            dp[i] = 0
        elif a[i] == 2 and dp[i-1] == 2:
            dp[i] = 0
        elif a[i] == 3 and dp[i-1] == 1:
            dp[i] = 2
        elif a[i] == 3 and dp[i-1] == 2:
            dp[i] = 1
        else:
            dp[i] = a[i]
        
ans = 0
for i in range(n):
    if dp[i] == 0:
        ans += 1
    
print(ans)

