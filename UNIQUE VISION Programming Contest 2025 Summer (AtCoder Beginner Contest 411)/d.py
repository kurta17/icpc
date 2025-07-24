from collections import defaultdict


n,q = map(int, input().split())
d = ['' for _ in range(n + 1)]
server = ''
for i in range(q):
    # print(d)
    qr = list(map(str, input().split()))
    if qr[0] == "2":
        d[int(qr[1])] += qr[2]
    elif qr[0] == "1":
        d[int(qr[1])] = server
    else:
        server = d[int(qr[1])]

print(server)
