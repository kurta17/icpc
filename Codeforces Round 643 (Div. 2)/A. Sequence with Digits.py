for _ in range(int(input())):
    a,k = map(int,input().split())
    ans = a
    for _ in range(k-1):
        a = str(ans)
        ans = int(a)+int(min(a))*int(max(a))
        if int(min(a)) == 0:
            break
    print(ans)

