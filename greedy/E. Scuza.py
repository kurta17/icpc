t = int(input())

for _ in range(t):
    n,q = map(int, input().split())
    st = list(map(int,input().split()))
    l = list(map(int,input().split()))

    ans = []
    pre = [st[0]]

    for i in range(1,n):
        pre.append(pre[i-1]+st[i])
    print(pre)

    for i in range(q):
        leg = l[i]
                
        ans.append(s)
    
    # print(" ".join(map(str,ans)))