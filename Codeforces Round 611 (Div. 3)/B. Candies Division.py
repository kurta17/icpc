import math

for _ in range(int(input())):
    n,k = map(int, input().split())

    eq = (math.ceil(n//k))
    rem = n - eq * k
    plus1 = math.ceil(k//2)
    used = min(plus1,rem)
    print(eq*k+used)

