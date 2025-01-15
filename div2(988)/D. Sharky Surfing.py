import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, L = map(int, input().split())
    union = []
    
    for _ in range(n):
        union.append((*list(map(int, input().split())), 1))
    
    for _ in range(m):
        union.append((*list(map(int, input().split())), 0))

    pow = []
    pp = 1

    union.sort()

    for a,b,p in union:
        if p == 0:
            heapq.heappush(pow,-b)
        else:
            while pow and pp < b-a+2:
                pp -= heapq.heappop(pow)
            if pp < b - a + 2:
                print(-1)
                break
    else:
        print(m-len(pow))