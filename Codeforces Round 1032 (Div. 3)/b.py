for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    seen = set()
    i, j = 1, n - 2
    turn = True
    seen.add(a[0])
    seen.add(a[-1])
    while i <= j:
        if turn == True:
            ch = a[i]
            i += 1
        else:
            ch = a[j]
            j -= 1
        if ch in seen:
            print("YES")
            break
        seen.add(ch)
        turn = not turn
    else:
        print("NO")
