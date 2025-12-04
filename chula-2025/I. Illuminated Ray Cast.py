import sys
input = sys.stdin.readline
 
for _ in range(int(input())):

    n = int(input())
    h = list(map(int, input().split()))
    x,y = map(int, input().split())
    besth = float('-inf')
    ans = 0
    
    for i in range(n):
        curh = h[i] * x - y * (i+1)
        if besth < curh:
            ans += 1
            besth = curh
    print(ans)