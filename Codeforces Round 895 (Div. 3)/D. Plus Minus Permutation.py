def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

for _ in range(int(input())):
    n,x,y = map(int,input().split())
    com_m = x*y//gcd(x,y)
    ssum = n // x - (n//com_m)
    minus = n // y - (n//com_m)
 
    print((2*n-ssum+1)*ssum//2 - (1+minus)*minus//2)


