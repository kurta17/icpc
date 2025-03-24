import bisect
n = int(input())
a = list(map(int, input().split()))

a.sort()

if n == 1:
    print(1)
else:
    prefsum = [a[0]]
    a = a[1:]
    ans = 1
    ind = 0

    while ind < n-1:
        ind = bisect.bisect_left(a,prefsum[-1])
        if ind < n-1:
            ans += 1
            prefsum.append(prefsum[-1] + a[ind])
            
    print(ans)
