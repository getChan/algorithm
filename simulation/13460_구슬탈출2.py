from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
board = []
for _ in range(n):
    board.append([x for x in input().rstrip()])
for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            b = (i, j)
        elif board[i][j] == 'R':
            r = (i, j)

answer = 11
def move(b, r, direction, level):
    global answer
    if level >= answer:
        return
    print(b, r, direction)
    ri, rj = r
    bi, bj = b

    if direction == 'left':
        while board[bi][bj-1] != '#':
            bj -= 1 
            if board[bi][bj] == 'O':
                return
        while board[ri][rj-1] != '#':
            rj -= 1
            if board[ri][rj] == 'O':
                if level < answer:
                    answer = level
                return
        if (ri, rj) == (bi, bj):
            if r[1] < b[1]:
                bj += 1
            else:
                rj += 1

    if direction == 'right':
        while board[bi][bj+1] != '#':
            bj += 1 
            if board[bi][bj] == 'O':
                return
        while board[ri][rj+1] != '#':
            rj += 1
            if board[ri][rj] == 'O':
                if level < answer:
                    answer = level
                return
        if (ri, rj) == (bi, bj):
            if r[1] < b[1]:
                rj -= 1
            else:
                bj -= 1

    if direction == 'up':
        while board[bi-1][bj] != '#':
            bi -= 1 
            if board[bi][bj] == 'O':
                return
        while board[ri-1][rj] != '#':
            ri -= 1
            if board[ri][rj] == 'O':
                if level < answer:
                    answer = level
                return
        if (ri, rj) == (bi, bj):
            if r[0] < b[0]:
                bi += 1
            else:
                ri += 1

    if direction == 'down':
        while board[bi+1][bj] != '#':
            bi += 1 
            if board[bi][bj] == 'O':
                return
        while board[ri+1][rj] != '#':
            ri += 1
            if board[ri][rj] == 'O':
                if level < answer:
                    answer = level
                return
        if (ri, rj) == (bi, bj):
            if r[0] < b[0]:
                ri -= 1
            else:
                bi -= 1

    r = (ri, rj)
    b = (bi, bj)
    for direction in ('left', 'right', 'up', 'down'):
        move(b, r, direction, level+1)

for direction in ('left', 'right', 'up', 'down'):
    move(b, r, direction, 1)

if answer > 10:
    print(-1)
else:
    print(answer)
print(dp)