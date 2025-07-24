n  = int(input())
a = list(map(int, input().split()))

i =  0
while i < n-1:
    cur = []
    cur.append(a[i])
    for j in range(i+1, n-1):
        cur.append(cur[-1] + a[j])
    print(*cur)
    i += 1
    