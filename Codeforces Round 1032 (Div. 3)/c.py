for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = []
    maxval = 0
    for i in range(n):
        a = list(map(int, input().split()))
        grid.append(a)

    vert_max = [0] * m
    for j in range(m):
        for i in range(n):
            vert_max[j] = max(vert_max[j], grid[i][j])

    row_max = [0] * n
    for i in range(n):
        row_max[i] = max(grid[i])
    
    valmax_row = 0
    count_row = 0
    for i in range(n):
        if row_max[i] > valmax_row:
            valmax_row = row_max[i]
            count_row = 1
        elif row_max[i] == valmax_row:
            count_row += 1
    
    valmax_col = 0
    count_col = 0   
    for j in range(m):
        if vert_max[j] > valmax_col:
            valmax_col = vert_max[j]
            count_col = 1
        elif vert_max[j] == valmax_col:
            count_col += 1
            
    print(valmax_row, valmax_col, count_row, count_col)
    if valmax_row > valmax_col and count_row == 1:
        print(valmax_row-1)
    elif valmax_col > valmax_row and count_col == 1:
        print(valmax_col-1)
    elif valmax_row == valmax_col and count_row <= 2 and count_col <= 2:
        print(valmax_row - 1)
    else:
        print(max(valmax_row, valmax_col))
