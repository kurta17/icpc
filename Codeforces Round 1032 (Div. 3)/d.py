t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = a + b
    total.sort()
    set_a = set()
    for i in range(0, 2 * n, 2):
        set_a.add(total[i])
    operations = []
    for i in range(n):
        if a[i] not in set_a:
            a[i], b[i] = b[i], a[i]
            operations.append((3, i + 1))
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                operations.append((1, j + 1))
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                operations.append((2, j + 1))
    print(len(operations))
    for op in operations:
        print(op[0], op[1])