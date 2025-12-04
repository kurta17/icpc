def gcd(a, b):
    if a == 0:
        return abs(b)
    return gcd(b % a, a)


import math
for _ in range(int(input())):
    a,b,k = map(int, input().split())
    need = max((a + k - 1) // k, (b + k - 1) // k)

    if need <= gcd(a,b):
        print(1)
    else:
        print(2)
    