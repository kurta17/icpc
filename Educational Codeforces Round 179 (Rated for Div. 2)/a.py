import math


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(3)
        continue
    s = math.ceil(math.log2(n))
    if math.pow(2,s) == n:
        print((s+1)*2+1)
    else:
        print(s*2+1)