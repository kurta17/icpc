n,k = map(int, input().split())
nums = list(map(int, input().split()))

pref = [0]

for i in range(n):
    pref.append(pref[-1] + nums[i])

ans = 0
if n == k:
    print(pref[-1]/n)

else:
    for j in range(k,n+1):
        for p in range(0,n-j+1):
            ans = max(ans, (pref[p+j] - pref[p])/j)
    print(ans)
