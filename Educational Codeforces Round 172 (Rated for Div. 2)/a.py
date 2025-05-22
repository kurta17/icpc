for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    ind = 0
    for i in range(n):
        k -= a[i]
        if k < 0:
            k += a[i]
            break
    print(k)
