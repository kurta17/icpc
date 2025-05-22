for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    maxx = max(a)
    minn = min(a)
    cnt_max = 0
    for i in a:
        if i == maxx:
            cnt_max += 1
            
    if maxx - minn > k+1  or (maxx - minn == k + 1 and cnt_max > 1) :
        print("Jerry")
    elif sum(a) % 2 == 0:
        print("Jerry")
    else:
        print("Tom")
        