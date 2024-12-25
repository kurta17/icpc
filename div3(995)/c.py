for _ in range(int(input())):
    n,m,k = map(int, input().split())
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))
    ans = []
    if n - k >= 2:
        print('0'*m)
    elif n == k:
        print('1'*m)
    else:
        dontknow = 0
        for i in range(1,n+1):
            if i > len(q) or i != q[i - 1]:
                dontknow = i
                break

        for i in range(1,m+1):
            if i != dontknow:
                ans.append('0')
            else:
                ans.append('1')

        print(''.join(ans))

