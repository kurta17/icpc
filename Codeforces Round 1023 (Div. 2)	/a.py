for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = max(a)

    if len(set(a)) >= 2:
        print("YES")
        ans = []
        for i in range(n):
            if b == a[i]:
                ans.append(2)
            else:
                ans.append(1)
        print(*ans)
    else:
        print("NO")