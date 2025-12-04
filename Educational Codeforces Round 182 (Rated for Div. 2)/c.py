for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 2
    for i in range(1,n):
        if min(a[i],b[i]) >= max(a[i-1],b[i-1]):
            ans *= 2
            ans %= 998244353
    print(ans)
            
