for _ in range(int(input())):
    n = int(input())
    if n % 2 != 0:
        print(" ".join(map(str, ([1] + [i for i in range(n,1,-1)]))))
    else:
        print(-1)