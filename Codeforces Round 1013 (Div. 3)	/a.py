for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cor = [0,1,0,3,2,0,2,5]
    have = []

    for i in range(n):
        if a[i] in cor:
            cor.remove(a[i])
        if len(cor) == 0:
            ans = True
            num = i+1
            break
    
    else:
        ans = False
    if ans:
        print(num)
    else:
        print(0)





