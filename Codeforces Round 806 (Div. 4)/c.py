for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    for ind in range(n):
        m,c = map(str, input().split())
        change = 0
        for i in range(int(m)):
            if c[i] == "U":
                change -= 1
            else:
                change += 1
        b[ind] += change
        b[ind] %= 10
    print(*b)