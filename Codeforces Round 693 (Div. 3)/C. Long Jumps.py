for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[-1] = a[-1]
    for i in range(n-2,-1,-1):
        if i + a[i] > n-1:
            dp[i] = a[i]
        else:
            dp[i] = a[i] + dp[i+a[i]]
    print(max(dp))
