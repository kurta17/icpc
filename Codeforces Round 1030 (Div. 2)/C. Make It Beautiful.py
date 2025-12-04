for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(60):
        for j in range(n):
            if a[j] % (2**(i+1)) != 0:
                count += 1
                a[j] -= 2**i
            elif k >= 2**i:
                count += 1
                k -= 2**i

    print(count)

