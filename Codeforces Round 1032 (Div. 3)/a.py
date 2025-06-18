for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    mmin = min(a)
    mmax = max(a)
    ddmin = abs(x - mmin) 
    ddmax = abs(x - mmax)
    if ddmin < ddmax:
        print(ddmin + (mmax - mmin))
    else:
        print(ddmax + (mmax - mmin))
