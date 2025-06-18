for _ in range(int(input())):
    n = int(input())
    ans = []

    for i in range(1,n+1,2):
        ans.append(i)
    if n % 2 == 0:
        for i in range(n, 0,-2):
            ans.append(i)
    else:
        for i in range(n-1, 0,-2):
            ans.append(i)
    print(*ans)
