t = int(input())

for _ in range(t):
    n = int(input())
    models = list(map(int, input().split()))
    dp = [1] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(2 * i, n + 1, i):
            if models[j - 1] > models[i - 1]:
                dp[j] = max(dp[j], dp[i] + 1)
    
    print(max(dp))