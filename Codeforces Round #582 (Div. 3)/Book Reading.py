import math


q = int(input())

for _ in range(q):
    n, m = map(int, input().split())
    num_cyc = math.floor((n // m // 10))
    last = []
    for i in range(1, 11):
        last.append((m * i) % 10)
    s = sum(last)
    print(s * num_cyc + sum(last[:math.floor((n // m)) % 10]))
