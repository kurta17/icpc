for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0]*n
    ans[0] = 1
    j = 2

    for i in range(1,n):
        if a[i] - i -1 == a[i-1]:
            ans[i] = j
            j += 1
        else:
            ans[i] = ans[i-(a[i] - a[i-1])]

        

    print(*ans)