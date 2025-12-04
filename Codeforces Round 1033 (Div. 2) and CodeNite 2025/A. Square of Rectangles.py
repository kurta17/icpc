import math


for _ in range(int(input())):
    l1,b1,l2,b2,l3,b3 = map(int, input().split())
    if l1+l2+l3 == b1 == b2 == b3:
        print("YES")
    elif b1+b2+b3 == l1 == l2 == l3:
        print("YES")
    elif b1 == l1+l2 == l1+l3 == b2+b3:
        print("YES")
    elif l1 == b1+b2 == b1+b3 == l2+l3:
        print("YES")
    else:
        print("NO")
