for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    suff = [0] * (n + 1)
    for k in range(1, n + 1):
        suff[k] = suff[k - 1] + a[n - k]
    
    pref_m = [0] * (n + 1)
    pref_m[0] = -10**18
    
    for m in range(1, n + 1):
        pref_m[m] = max(pref_m[m - 1], a[m - 1])
    
    ans = []
    for k in range(1, n + 1):
        ans.append(max(suff[k], suff[k - 1] + pref_m[n - k]))
    
    print(*ans)