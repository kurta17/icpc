for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    l = []
    for i in range(n):
        if a[i] <= k:
            l.append(1)
        else:
            l.append(-1)
    pref = [l[0]]
    for i in range(1,n):
        pref.append(pref[-1] + l[i])
    suff = [l[-1]]
    for i in range(n-2,-1,-1):
        suff.append(suff[-1] + l[i])
    ans = False
    suffcnt = 0
    prefcnt = 0
    for i in range(n):
        if suff[i] >= 0:
            suffcnt += 1
        if pref[i] >= 0:
            prefcnt += 1
        if (suffcnt >= 2 or prefcnt >= 2) and (prefcnt>0 and suffcnt>0):
            ans = True
            break
    if ans:
        print("YES")
    else:
        print("NO")


    


        
    

