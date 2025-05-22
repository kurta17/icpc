for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    a = [0]
    for i in range(1,n):
        if s[i-1] != s[i]:
            a.append(s[i-1])
   
    a.append(s[-1])
    a.append(0)
    ans = 0
    for i in range(1,len(a)-1):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            ans += 1
    if len(a) <= 2:
        print(1)
    print(ans)