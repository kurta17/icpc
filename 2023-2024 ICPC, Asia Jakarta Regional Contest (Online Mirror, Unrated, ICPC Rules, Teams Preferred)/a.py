row1 = list(input())
row2 = list(input())
row3 = list(input())
grid = []
letters = {'A':1 , 'B' : 2, 'C': 3}
grid.append(row1)
grid.append(row2)
grid.append(row3)
ans = 'CCC'
min_lex = 100
for i in range(3):
    for j in range(3):
        possible_squares = [(i,j+1), (i-1,j+1),(i-1,j), (i-1,j-1),(i,j-1),(i+1,j-1), (i+1,j),(i+1,j+1)]
        for ind in range(8):
            if possible_squares[ind][0] < 0 or possible_squares[ind][0]>2 or possible_squares[ind][1] <0 or possible_squares[ind][1] >2:
                possible_squares[ind] =(None,None)
        for x,y in possible_squares :
            if (x,y) !=(None,None):
                new_possible_squares = [(x,y+1), (x-1,y+1),(x-1,y), (x-1,y-1),(x,y-1),(x+1,y-1), (x+1,y),(x+1,y+1)]
                for indx in range(8):
                    if new_possible_squares[indx][0] < 0 or new_possible_squares[indx][0]>2 or new_possible_squares[indx][1] <0 or new_possible_squares[indx][1] >2 or (new_possible_squares[indx][0] ==i and new_possible_squares[indx][1] == j):
                        new_possible_squares[indx] = (None,None)
                for new_indx in range(8):
                    if new_possible_squares[new_indx] !=(None,None):
                            cur_ans = grid[i][j] + grid[x][y] + grid[new_possible_squares[new_indx][0]][new_possible_squares[new_indx][1]]
                            for k in range(3):
                                if letters[ans[k]] < letters[cur_ans[k]]:
                                    break
                                elif letters[ans[k]] >letters[cur_ans[k]]:
                                    ans = cur_ans
                                    break


print(ans)





