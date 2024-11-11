import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        avv = math.ceil(sum(a) / (n))
    
        if avv == a[0] and avv == a[-1]:
            print(0)
        elif avv > a[0] and a[-1] < avv:
            print(avv+((avv-a[0]) // n + 1) - a[0])
        elif avv > a[0] and avv < a[-1]:
            print(a[-1] - a[0])
        elif a[0] > avv and a[-1] > avv:
            print(avv+((avv-a[0]) // n) - a[0])
        else:
            print(1)
        
