for _ in range(int(input())):
    n, m = map(int, input().split())
    if n - m + 1 >= 0 and (n - m + 1) % 9 == 0:
        print('YES')
    else:
        print('NO')