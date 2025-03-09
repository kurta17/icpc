n = int(input())
ang = []

for _ in range(n):
    ang.append(int(input()))

for mask in range(1 << n):
    tot = 0
    for i in range(n):
        if mask & (1 << i):
            tot -= ang[i]
        else:
            tot += ang[i]
    if tot % 360 == 0:
        print("YES")
        break
else:
    print("NO")




