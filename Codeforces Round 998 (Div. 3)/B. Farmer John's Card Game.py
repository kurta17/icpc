for _ in range(int(input())):
    n,m = map(int,input().split())
    rounds = []
    ans = True
    for _ in range(n):
        cow = list(map(int,input().split()))
        cow.sort()
        for i in range(1,m):
            if cow[i] != cow[i-1]+n:
                ans = False
        rounds.append(cow)
        
    if not ans:
        print(-1)
    else:
        res = []
        for i in range(n):
            for j in range(n):
                if rounds[j][0] == i:
                    res.append(j+1)
                    
        print(*res)



    