for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [1]
    for i in range(1,n-1):
        if a[i-1] >= a[i]:
            ans.append(1)
        else:
            ans.append(0)
    ans.append(1)
    print(ans)