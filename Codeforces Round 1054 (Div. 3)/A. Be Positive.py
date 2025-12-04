for _ in range(int(input())):
    n = int(input())
    zero = 0
    negone = 0
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == -1:
            negone += 1
        elif a[i] == 0:
            zero += 1
    plus = negone % 2
    print(zero + plus*2)