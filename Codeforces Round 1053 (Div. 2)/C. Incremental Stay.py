for _ in range(int(input())):
    n = int(input()) * 2
    a = list(map(int, input().split()))
    if n == 2:
        print(a[1]-a[0])
        continue

    ans1 = 0
    for i in range(n):
        if i % 2 == 0:
            ans1 -= a[i]
        else:
            ans1 += a[i]
    ans2 = -a[0] + a[-1]
    for i in range(1,n-1):
        if i % 2 == 0:
            ans2 += a[i]
        else:
            ans2 -= a[i]

    ans = [ans1,ans2]
    for i in range(2,n//2):
        curr = ans[i-2] - 2 * a[i-1] + 2 * a[n-i]
        # print(a[i-1])
        # print(a[n-i])
        ans.append(curr)
    print(*ans)
    