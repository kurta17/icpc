for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    dp=[0] * (n)
    dp[0] = abs(a[0])
    for i in range(1,n):
        if a[i] * a[i-1] > 0 or (a[i-1] > 0 and a[i] < 0):
            dp[i] = abs(a[i]) + dp[i-1]
        else:
            dp[i] = abs(a[i]) + d[i-1]
    
    print(max(dp))