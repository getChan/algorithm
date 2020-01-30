from copy import deepcopy
FINISH = False
sudoku = []
for _ in range(9):
    sudoku.append([int(x) for x in input().split()])

# 다음 세 가지 조건으로 경우의 수 좁힌 뒤 완전탐색
# 1. 가로줄
# 2. 세로줄
# 3. 3X3 정사각형
def search(sudoku, si, sj):
    global FINISH
    if FINISH:
        return
    for i in range(si, 9):
        for j in range(9):
            if FINISH:
                return
            if sudoku[i][j] == 0:
                candidate = {x for x in range(1, 10)}
                for x in range(9):
                    candidate.discard(sudoku[i][x])
                for y in range(9):
                    candidate.discard(sudoku[y][j])
                for by in range((i//3)*3, (i//3+1)*3):
                    for bx in range((j//3)*3, (j//3+1)*3):
                        candidate.discard(sudoku[by][bx])
                
                for can in candidate:
                    if FINISH:
                        return
                    newdoku = list(map(list, sudoku))
                    newdoku[i][j] = can
                    newdoku = tuple(list(map(tuple, newdoku)))
                    search(newdoku, i, j)
                else:
                    return

    else:
        for row in sudoku:
            for item in row:
                print(item, end=' ')
            print()
        FINISH = True
        

search(tuple(list(map(tuple, sudoku))), 0, 0)