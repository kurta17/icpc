for _ in range(int(input())):
    n, x, y = map(int,input().split())
    a = [-1 for i in range(n)]
    for i in range(y-1,x):
        a[i] = 1
    print(*a)
