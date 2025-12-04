for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    curr = a[k-1]
    a.sort()
    level = 1
    ans = True
    for i in range(n):
        if a[i] > curr:
            level += a[i] - curr
            if level - 1 > curr:
                ans = False 
                break
            curr = a[i]
    if ans:
        print("YES")
    else:
        print("NO")