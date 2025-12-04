for _ in range(int(input())):
    n = int(input())
    ans = 0
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1,n,2):
        ans = max(ans, a[i] - a[i-1])
    print(ans)