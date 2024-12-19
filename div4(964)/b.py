t=int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    ans=0

    for i in range(2):
        if (a>c)+(b>d)>(a<c)+(b<d):
            ans+=2
        a,b = b,a

    print(ans)