for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    c = a[1] - a[0]
    diff_eq = True
    for i in range(1, n - 1):
        if a[i + 1] - a[i] != c:
            diff_eq = False
            break
    
    if diff_eq:
        d = a[0] - c
        if d >= 0 and d % (n + 1) == 0:
            k_1 = c + d // (n + 1)
            if k_1 >= 0:
                ans = "YES"
            else:
                ans = "NO"
        else:
            ans = "NO"
    else:
        ans = "NO"
    
    print(ans)