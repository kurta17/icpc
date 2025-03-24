from collections import defaultdict

n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = []
d = defaultdict(int)

for i in range(n):
    if a[i] not in d:
        d[a[i]] = i+1
        ans.append(i+1)
if len(d)<k:
    print("NO")
else:
    print("YES")
    print(*ans[:k])