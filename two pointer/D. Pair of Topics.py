n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0

diff = []
for i in range(n):
    diff.append(a[i]-b[i])

diff.sort()

i, j = 0, n - 1
while i < j:
    if diff[i] + diff[j] > 0:
        ans += (j - i)
        j -= 1
    else:
        i += 1
print(ans)


