import math


for _ in range(int(input())):
    n = int(input())
    k = 1
    while n > 3:
        n = n//4
        k*=2
    print(k)