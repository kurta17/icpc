from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
   
    if n == 1:
        print(1)
    elif n == 2:
        if a[0] == a[1]:
            print(1)
        else:
            print(2)
    else:
        x=a[0]
        m = n
        for i in range(1,n-1):
            if x<=a[i]<=a[i+1]:
                m-=1
            elif x>=a[i]>=a[i+1]:
                m-=1
            else:
                x=a[i]
        if x == a[-1]:
            m-=1
        print(m)



