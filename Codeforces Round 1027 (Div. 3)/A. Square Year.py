import math


for _ in range(int(input())):
    n = int(input())
    s = int(math.sqrt(n))
    if s * s == n:
        print(0,s)
    else:
        print(-1)
    