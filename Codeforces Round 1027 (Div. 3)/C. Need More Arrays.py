for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    i = 0
    j = 1
    while i < n and j < n:
        if a[j] > a[i] + 1:
            ans += 1
            i = j
        j += 1
    print(ans)

