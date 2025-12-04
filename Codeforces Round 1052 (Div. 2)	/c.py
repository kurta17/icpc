for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip()))
    ans = [-1] * n
    r = []
    st = True
    f = 1
    l = -1
    end = False

    for i in range(n):
        if a[i] == 1 and not st:
            ans[i] = i+1
            f = i+1
            st = True
        elif a[i] == 1 and not end:
            ans[i] = i+1
            l = i+1
            r.append((f,l))
            st= True
            f = i+1
            end = False


    if r[-1][1] != n:
        r.append((r[-1][1],n))

    for start, end in (r[:-1]):
        current_num = end - 1
        for i in range(start-1, end):
            if ans[i] == -1:
                ans[i] = current_num
                current_num -= 1
    s,e = r[-1]
    last = e
    for i in range(s,e):
        ans[i] = last
        last -= 1

    for i in range(n):
        if ans[i] == i + 1 and a[i] == 0:
            print("NO")
            break
    else:
        print("YES")
        print(*ans)