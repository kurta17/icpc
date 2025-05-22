from collections import defaultdict
import math


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for i in a:
        d[i] += 1

    u = 0
    k = 0 
    for i in d:
        if d[i] == 1:
            u += 1
        else:
            k += 1
    
    print(2 * math.ceil(u / 2) + k)