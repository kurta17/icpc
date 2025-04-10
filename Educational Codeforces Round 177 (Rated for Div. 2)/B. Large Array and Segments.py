for _ in range(int(input())):
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    darch = x % s
    i = -1
    c = 0
    while darch > 0:
        darch -= a[i]
        i-=1
        c += 1
    print(max(n*k - x // s * n - c +1,0))
