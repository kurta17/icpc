from bisect import bisect_left

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    part = list(map(int, input().split()))
    prob = list(map(int, input().split()))
    kev = part[0]
    ranks = sorted(part[1:])

    solved_until = bisect_left(prob,kev)
    better_untill = bisect_left(ranks,kev)

    prob.sort()
   
    for i in range(1,n+1):
        ans = 0
        for j in range(0,n,i):
            max_sirt = prob[j]
            if max_sirt < kev:
                ans += 1
            else:
                ans += n - better_untill -1
    
        print(ans)

        



    