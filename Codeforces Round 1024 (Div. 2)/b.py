import math


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    less = 0
    more = 0
    for i in range(1,n):
        if abs(a[i]) <= abs(a[0]):
            less += 1
        
    if less <= math.floor(n/2):
        print("YES")
    else:
        print("NO")