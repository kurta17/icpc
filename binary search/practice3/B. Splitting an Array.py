n,k = map(int, input().split())
a = list(map(int, input().split()))

def poss(ms,a,k):
    cnt = 1
    curr_sum = 0
    for i in a:
        if curr_sum + i > ms:
            curr_sum = i
            cnt += 1
        else:
            curr_sum += i
    return cnt <= k

l = 0
r = sum(a)

while r > l:
    mid = (l+r)//2
    if poss(mid,a,k):
        r = mid
    else:
        l = mid + 1
print(l)

