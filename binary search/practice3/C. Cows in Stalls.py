n,k = map(int, input().split())
a = list(map(int, input().split()))

def check(dis,a,k):
    st = a[0]
    curr = 0
    cnt = 1
    for i in range(n):
        curr=(a[i] - st)
        if curr >= dis:
            curr = 0
            st = a[i]
            cnt += 1
    return cnt >= k

l = 0 
r = 10**9 + 1
while r > l + 1:
    mid = (l+r)//2
    if check(mid,a,k):
        l = mid
    else:
        r = mid

print(l)
