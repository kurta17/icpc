n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
ans = []

while i < max(n,m):
    if i < n and i < m:
        if a[i] > b[i]:
            ans.append(b[i])
            ans.append(a[i])
        else:
            ans.append(a[i])
            ans.append(b[i])
    elif i < n:
        ans.append(a[i])
    elif i < m:
        ans.append(b[i])
    i+=1

print(*ans)