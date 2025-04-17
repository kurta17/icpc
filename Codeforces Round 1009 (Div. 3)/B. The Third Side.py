for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        print(a[0])
    elif n == 2:
        print(a[0] + a[1] - 1)
    else:
        el = a[0] + a[1] - 1
        for i in range(2,n):
            el += a[i] - 1
        print(el)