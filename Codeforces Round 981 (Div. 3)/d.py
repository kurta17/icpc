import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prf = [0] * (n+1)
    mp = {0:0}
    lst = [-1] * (n + 1)
    for i in range(1,n+1):
        prf[i] = prf[i-1] + a[i-1]
        if prf[i] in mp:
            lst[i] = mp[prf[i]]
        mp[prf[i]] = i
        
    dp = [0] * (n+1)
    for i in range(1,n+1):
        dp[i] = dp[i-1]
        if lst[i] != -1: 
            dp[i] = max(dp[i], dp[lst[i]] + 1)

    print(dp[-1])