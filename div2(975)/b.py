from collections import defaultdict
t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    x = list(map(int,input().split()))
    quer = list(map(int,input().split()))

    segm_count = defaultdict(int)
    for i in range(n):
        if i != n-1:
            segm_count[(i+1)*(n-i-1)] += (x[i+1]-x[i]-1)
            segm_count[(i)*(n-i-1) + (n-1)] += 1
        else:
            segm_count[n-1] +=1
            

    ans = [segm_count[k] for k in quer]
    
    print(' '.join(map(str, ans)))
