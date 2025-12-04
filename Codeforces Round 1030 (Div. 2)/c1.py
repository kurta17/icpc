def sumbase3dig(x):
    s = 0
    while x:
        s += x % 3
        x //= 3
    return s

for _ in range(int(input())):
    n_str = input().strip().split()
    n = int(n_str[0])
    k = int(n_str[1])

    s = sumbase3dig(n)
    if k < s:
        print(-1)
        continue

    m = min(k, n)
    if (m % 2) != (n % 2):
        m -= 1
    if m < s:
        print(-1)
        continue

    rr = (n - m) // 2
    extra = 0
    cur = n
    pow3 = 1
    while cur >= 3 and rr > 0:
        m_i = cur // 3
        take = m_i if m_i <= rr else rr
        extra += take * pow3
        rr -= take
        cur = m_i
        pow3 *= 3

    ans = 3 * n + extra
    print(str(ans))
