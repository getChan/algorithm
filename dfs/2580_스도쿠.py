from pprint import pprint
sudoku = []
for i in range(9):
    sudoku.append([int(_) for _ in input().split()])

# 1. 가로로 쭉 본다
# 2. 세로로 쭉 본다
# 3. 3*3으로 본다
nominate = [[0 for _ in range(9)] for _ in range(9)]

i = 0
while i < 9:
    j = 0
    while j < 9:
        if sudoku[i][j] == 0:
            tmp = {_ for _ in range(1,10)}
            # 1. 
            col = 0
            while col<9:
                if sudoku[i][col] != 0:
                    tmp.discard(sudoku[i][col])
                col += 1
            # 2. 
            row = 0
            while row<9:
                if sudoku[row][j] != 0:
                    tmp.discard(sudoku[row][j])
                row += 1
            # 3. 
            if i < 3:
                row = 0
                if j < 3:
                    col = 0
                elif j < 6:
                    col = 3
                else:
                    col = 6
            elif i < 6:
                row = 3
                if j < 3:
                    col = 0
                elif j < 6:
                    col = 3
                else:
                    col = 6
            else:
                row = 6
                if j < 3:
                    col = 0
                elif j < 6:
                    col = 3
                else:
                    col = 6
            for _ in range(3):
                for __ in range(3):
                    if sudoku[row+_][col+__] != 0:
                        tmp.discard(sudoku[row+_][col+__])
            nominate[i][j] = tmp
        j += 1
    i+= 1
pprint(nominate)