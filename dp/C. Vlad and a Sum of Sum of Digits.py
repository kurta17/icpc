dp = [0] * (2 * 10**5+1)

for k in range(1,2 * 10**5+1):
    res = 0
    i = k
    while i >= 1:
        res += (i % 10)

        i = i // 10
    dp[k] = res

pref = [0,dp[1]]

for j in range(2,2 * 10**5+1):
    pref.append(pref[j-1] + dp[j])

for _ in range(int(input())):
    n = int(input())
    print(pref[n])