for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    two = False

    for i in range(n):
        if i+1 == a[a[i]-1]:
            two = True
    
    if two:
        print(2)
    else:
        print(3)