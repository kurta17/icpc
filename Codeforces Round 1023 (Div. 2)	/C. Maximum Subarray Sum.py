for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    a = list(map(int, input().split()))

    INF = 10**18
    b = [a[i] if s[i] == '1' else -INF for i in range(n)]

    curr = b[0]
    gen_res = b[0]
    for x in b[1:]:
        curr = max(x, curr + x)
        gen_res = max(gen_res, curr)

    zero_positions = [i for i, ch in enumerate(s) if ch == '0']
    if gen_res > k or (gen_res != k and not zero_positions):
        print("NO")
        continue

    if not zero_positions:
        print("YES")
        print(*a)
        continue

    pos = zero_positions[0]

    curr = 0
    L = 0
    for i in range(pos + 1, n):
        curr = max(b[i], curr + b[i])
        L = max(L, curr)

    curr = 0
    R = 0
    for i in range(pos - 1, -1, -1):
        curr = max(b[i], curr + b[i])
        R = max(R, curr)

    a[pos] = k - L - R
    for i in zero_positions:
        if i != pos:
            a[i] = -INF

    print("YES")
    print(*a)
