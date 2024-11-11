n = int(input())  
a = list(map(int, input().split()))  

in_sum = sum(a)  

if in_sum == n:
    print(n - 1)
    exit()

dp = [1 if x == 0 else -1 for x in a]

max_flip = dp[0]
current_sum = dp[0]

for i in range(1, n):
    current_sum = max(dp[i], current_sum + dp[i])
    max_flip = max(max_flip, current_sum)

print(in_sum + max_flip)
