a = list(map(int, input().split()))
prob = ['A', 'B', 'C', 'D', 'E']

comb_s = []
for i in range(1, 32):
    s = 0
    n = ""
    for j in range(5):
        if (i >> j) & 1:
            s += a[j]
            n += prob[j]
    comb_s.append((s, n))

comb_s.sort(key=lambda x: (-x[0], x[1]))

for _, n in comb_s:
    print(n)