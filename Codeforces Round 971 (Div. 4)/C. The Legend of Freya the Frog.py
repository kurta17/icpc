for _ in range(int(input())):
    a,b,k = map(int,input().split())
    print(max(2*((a+k-1)//k)-1,2*((b+k-1)//k)))
   