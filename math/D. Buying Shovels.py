import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    if k >= n:
        print(1)
        continue
    
    min_packages = n  
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            if i <= k:
                min_packages = min(min_packages, n // i)
            if n // i <= k:
                min_packages = min(min_packages, i)
    
    print(min_packages)
