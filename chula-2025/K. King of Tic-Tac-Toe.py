def win(b):
    # check all 8 win lines
    lines = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]
    for l in lines:
        if all(b[x][y] == 'O' for x, y in l):
            return True
    return False


for _ in range(int(input())):
    grid = []
    empty = []
    for i in range(3):
        row = list(input().strip())
        grid.append(row)
        for j in range(3):
            if row[j] == '.':
                empty.append((i, j))

    found =False

    for i in range(len(empty)):
        for j in range(i+1, len(empty)):
            (x1, y1) = empty[i]
            (x2, y2) = empty[j]

            temp = [row[:] for row in grid]
            temp[x1][y1] ='O'
            temp[x2][y2]= 'O'

            if win(temp):
                print("YES")
                for r in temp:
                    print("".join(r))
                found = True
                break
        if found:
            break

    if not found:
        print("NO")
