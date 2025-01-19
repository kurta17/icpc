for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ndel = float('inf')

    for i in range(n):
        cur = i
        for j in range(i,n):
            if a[i] < a[j]:
                cur += 1
        
        if ndel > cur:
            ndel = cur
    print(ndel)

    