for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ptr = 0
    preff = [-1] * m
    for i in range(n):
        if ptr < m and a[i] >= b[ptr]:
            preff[ptr] = i
            ptr += 1
    if ptr == m:
        print(0)
        continue
    print(preff)
    suff = [-1] * m
    ptr = m - 1
    for i in range(n-1, -1, -1):
        if ptr >= 0 and a[i] >= b[ptr]:
            suff[ptr] = i
            ptr -= 1
    print(suff)
    min_k = float('inf')
    for j in range(m):
        poss = False
        if j == 0:
            if m == 1:
                poss = True
            else:
                if suff[1] != -1:
                    poss = True
        elif j == m-1:
            if preff[j-1] != -1:
                poss = True
        else:
            if preff[j-1] != -1 and suff[j+1] != -1 and preff[j-1] < suff[j+1]:
                poss = True
        if poss:
            min_k = min(min_k, b[j])

    if min_k == float('inf'):
        print(-1)
    else:
        print(min_k)
