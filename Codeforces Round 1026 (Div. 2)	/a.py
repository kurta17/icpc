for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = float('inf')
    for i in range(n):
        for j in range(n-1,-1,-1):
            if (a[i] + a[j]) % 2 == 0:
                ans = min(ans,i + n - j-1)
    
    print(ans)