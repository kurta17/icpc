import math

def num_max_desk(m, x):
    return m // (x + 1) * x +  m % (x + 1)

def place(n, m, k, x):
    return n * num_max_desk(m, x) >= k

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    l = 1
    r = m
    while l < r:
        mid = l + (r - l) // 2
        if place(n, m, k, mid):
            r = mid 
        else:
            l = mid + 1
    
    print(l)