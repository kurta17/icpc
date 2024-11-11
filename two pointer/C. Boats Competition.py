from typing import Counter


t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int,input().split()))

    count = Counter(w)
    max_w = 2*n
    ans = 0
    
    for tot in range(2,max_w+1):
        curr = 0
        
        for i in range(1,(tot+1)//2):
            if tot-i > n:
                continue
            curr += min(count[i],count[tot-i])

        if tot%2 == 0:
            curr += count[tot//2]//2

        ans = max(ans,curr)

    print(ans)
   