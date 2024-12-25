from bisect import bisect_right, bisect_left
for _ in range(int(input())):
    n,x,y = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    good_pairs = 0
    ss = sum(a)
    
    for i in range(n):
        darch = ss - a[i]
        if darch < x:
            continue
        mmax = darch - x
        mmin = darch - y
        min_index = bisect_left(a, mmin, i+1)
        max_index = bisect_right(a, mmax, i+1) - 1
        if min_index <= max_index:
            good_pairs += max_index - min_index + 1
    
    print(good_pairs)
