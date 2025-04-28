for _ in range(int(input())):
    n,x = map(int,input().split())
    
    if x != 0 and n != 1:
        ans = []
        for i in range(1,x):
            ans.append(i)
        ans.append(0)
        for j in range(n-1,x-1,-1):
            ans.append(j)
        print(*ans)
    elif n == 1 and x != 0:
        print(x-1)
    elif x == 0:
        ans = [i for i in range(n-1,-1,-1)]
        print(*ans)
    
