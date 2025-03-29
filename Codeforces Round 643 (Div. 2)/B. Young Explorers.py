from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = defaultdict(int)

    for i in a:
        d[i]+=1

    darch = 0
    ans = 0
    d = sorted(d.items(), key=lambda x: x[0])

    for i,j in d:
        ans += (j + darch) // i
        darch = (j + darch) % i

    print(ans)