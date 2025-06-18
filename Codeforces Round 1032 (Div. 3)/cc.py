for _ in range(int(input())):
    n, m = map(int, input().split())
    t = []
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(m):
            t.append([a[j], i, j])

    # sort the list of tuples based on the first element (the value)
    t.sort(reverse=True, key=lambda x: x[0])
    # print(t)
    valij = t[0][0]

    rowchosen = t[0][1]
    ansrow = valij - 1
    colchosen = -1
    for i in range(1,len(t)):
        if t[i][0] == valij:
            if t[i][1] != rowchosen:
                if colchosen == -1:
                    colchosen = t[i][2]
                else:
                    if t[i][2] != colchosen:
                        ansrow = valij
        else:
            break
    
    anscol = valij - 1
    colch = t[0][2]
    rowch = -1
    for i in range(1, len(t)):
        if t[i][0] == valij:
            if t[i][2] != colch:
                if rowch == -1:
                    rowch = t[i][1]
                else:
                    if t[i][1] != rowch:
                        anscol = valij
        else:
            break
    print(min(ansrow, anscol))
    # print(rowchosen, colchosen, ansrow)
    # print(colchosen, rowch, anscol)

    