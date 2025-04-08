for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = []
    if n == 2:
        print(a[0],a[1])
    else:
        diff = float('inf')
        l,r = 0,0
        for i in range(1,n):
            if a[i]-a[i-1] < diff:
                diff = a[i]-a[i-1]
                l = i-1
                r = i
        print(*a[r:],*a[:l+1])