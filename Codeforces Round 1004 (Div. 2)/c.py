for _ in range(int(input())):
    n = int(input())
    for i in range(10):
        x = n - i
        curstep = float('inf')

        while x:
            # print(x)
            c = x % 10
            cur = (7-c)%10
            curstep = min(cur, curstep)
            x //= 10
        curstep = min(curstep,7)
        if curstep <= i:
            print(i)
            break

    