t = int(input())

for _ in range(t):
    n = int(input())
    mat = [list(map(int, input().split())) for i in range(n)]
    op = 0
    diagonals = {}
    
    for i in range(n):
        for j in range(n):
            if mat[i][j] < 0: 
                diag_ind = i - j
                if diag_ind not in diagonals:
                    diagonals[diag_ind] = []
                diagonals[diag_ind].append((i, j))
    
    for diag_cells in diagonals.values():
        min_op = max(-mat[i][j] for i, j in diag_cells)
        op += min_op

    print(op)
