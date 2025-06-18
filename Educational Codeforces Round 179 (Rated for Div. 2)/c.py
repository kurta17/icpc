for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if len(set(a)) == 1:
        print(0)
        continue
    ans = float('inf')
    i = 0
    while i < n:

        j = i
        while j < n and a[j] == a[i]:
            j += 1
        
        ans = min(ans, (i + n - j) * a[i])
        i = j
        
    print(ans)