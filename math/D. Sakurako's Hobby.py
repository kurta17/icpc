t = int(input())
for _ in range(t):
    n = int(input())
    b = [0] * (n + 1)
    us = [0] * (n + 1)
    p = [k-1 for k in map(int, input().split())]
    s = input()

    cycle = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            cycle.append([i])
            visited[i] = True
            j = p[i]
            while j != i:
                cycle[-1].append(j)
                visited[j] = True
                j = p[j]

    for c in cycle:
        sz = sum(s[i] == '0' for i in c)
        for i in c:
            b[i] = sz

    print(" ".join(map(str, b[:-1])))
