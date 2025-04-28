for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_a = min(a)
    max_a = max(a)

    non_miss = [a[i] + b[i] for i in range(n) if b[i] != -1]

    if len(set(non_miss)) > 1:
        print(0)
    elif len(non_miss) == 0:
        print(max(0, min_a + k - max_a + 1))
    else:
        x = non_miss[0]
        if x < max_a or x > min_a + k:
            print(0)
        else:
            print(1)