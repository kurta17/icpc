for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    pref = [0] * n
    suff = [0] * n
    pref[0] = a[0] if a[0] > 0 else 0
    suff[n-1] = abs(a[n-1]) if a[n-1] < 0 else 0
    for i in range(1,n):
        pref[i] = pref[i-1]
        if a[i] > 0:
            pref[i] = pref[i-1] + a[i]
        
    
    for i in range(n-2,-1,-1):
        suff[i] = suff[i+1]
        if a[i] < 0:
            suff[i] = suff[i+1] + abs(a[i])
    ans = 0
    for i in range(n):
        ans = max(ans, pref[i] + suff[i])
    print(ans)
    