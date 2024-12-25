for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] > b[i+1]:
            ans += a[i] - b[i+1]
    ans += a[-1]
    print(ans)
