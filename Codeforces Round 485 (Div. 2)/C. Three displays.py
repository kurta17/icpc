n = int(input())
s = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = float('inf')

for j in range(1,n-1):
    unt_min = float('inf')
    for i in range(j):
        if s[i] < s[j]:
            unt_min = min(unt_min, c[i])

    next_min = float('inf')
    for k in range(i+1,n):
        if s[k] > s[j]:
            next_min = min(next_min, c[k])

    ans = min(ans, c[j] + unt_min + next_min)
if ans == float('inf'):
    print(-1)
else:
    print(ans)