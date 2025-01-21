import math
def euclid(a,b):
    if b ==0:
        return a
    return euclid(b, a%b)

n = int(input())
a = list(map(int, input().split()))

ngcd = a[0]

for i in range(1,n):
    ngcd = euclid(ngcd, a[i])

ans = 0

for i in range(1, int(math.sqrt(ngcd)+1)):
    if ngcd % i == 0:
        ans += 1
        if i != ngcd//i:
            ans += 1

print(ans)