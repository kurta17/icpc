for _ in range(int(input())):
    n,k = (map(int, input().split()))
    a = set(map(int, input().split()))
    if len(a) > k:
        print(-1)
    else:
        for i in range(1,n+1):
            if len(a) == k:
                break
            elif i not in a:
                a.add(i)
        print(n*k)
        print(*(list(a) * n))
    
