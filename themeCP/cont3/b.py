for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    dist = 0
    for i in range(1,n):
        dist += (a[i] - a[i-1]-1)
    print("YES") if dist<=2 else print("NO")
       