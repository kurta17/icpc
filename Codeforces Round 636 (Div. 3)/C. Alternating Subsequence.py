for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pos = True if a[0] > 0 else False
    ans = []
    i = 0
    el = a[0]
    for i in range(n):
        if a[i] > 0 and pos:
            el = max(el, a[i])
        elif a[i] > 0 and not pos:
            ans.append(el)
            el = a[i]
            pos = True
        elif a[i] < 0 and not pos:
            el = max(el, a[i])
        else:
            ans.append(el)
            el = a[i]
            pos = False
    if (a[-1] > 0 and pos) or (a[-1] < 0 and not pos):
        ans.append(el)
    print(sum(ans))

