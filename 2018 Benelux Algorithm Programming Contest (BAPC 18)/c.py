import math


n = int(input())
ans = float('inf')
if n == 1:
    print(6)
else:
    for a in range(1,int(math.floor(math.pow(n,1/3)))+2):
        if n % a == 0:
            m = n // a
            for b in range(1,int(math.floor(m ** 1/2))+2):
                if m % b == 0:
                    c = m // b
                    ans = min(ans, 2 * (a*b + a*c + b*c))

    print(ans)
