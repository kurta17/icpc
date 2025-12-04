for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * (n+1)
    for i in a:
        d[i] += 1
    for j in range(n):
        if d[j] > 2:
            d[j+1] += d[j] - 2
            d[j] = 2

    for i in d:
        if i % 2 != 0:
            print("NO")
            break
    else:
        print("YES")

