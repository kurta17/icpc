for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    i = 0
    skip = 0
    while i < n:
        found = False
        if i + k < n+1:
            for j in range(i,i+k):
                if a[j] == 1:
                    found = True
                    skip = j
            if found:
                i = skip+1
            else:
                ans += 1
                i += k + 1
        else:
            break
    print(ans)