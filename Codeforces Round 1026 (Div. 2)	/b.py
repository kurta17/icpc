for _ in range(int(input())):
    s = list(map(str, input().strip()))
    n = len(s)
    ans = False
    opens = 1
    closed = 0
    for i in range(1,n):
        if s[i] == '(':
            opens += 1
        else:
            closed -= 1
        if closed + opens == 0 and i != n - 1:
            ans = True
            break

    print("YES" if ans else "NO")