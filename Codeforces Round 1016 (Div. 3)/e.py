def check(targ):
    subs = 0
    exist = set()
    i = 0
    while i < len(a):
        if targ > a[i]:
            exist.add(a[i])
        if len(exist) == targ:
            exist.clear()
            subs += 1
        i += 1
    return subs >= k


for _ in range(int(input())):
    x,k = (map(int,input().split()))
    a = list((map(int,input().split())))
    l = 0
    r = x + 1

    while l<r:
        mid = (l+r) // 2
        if check(mid):
            l = mid + 1
        else:
            r = mid

    print(l-1)