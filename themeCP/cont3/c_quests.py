for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    msub = b[0]
    cursum = 0
    i = 0
    ans = 0
    
    while i < n and i < k:
        cursum += a[i]
        if msub < b[i]:
            msub = b[i]
        ans = max(ans,cursum + (k - i - 1)*msub)
        i += 1

    print(ans)
