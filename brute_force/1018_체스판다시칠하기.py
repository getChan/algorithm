def min_square(i, j):
    global board
    cnt_w, cnt_b = 0, 0
    origin = ['WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW']
    for a in range(8):
        for b in range(8):
            if origin[a][b] != board[i+a][j+b]:
                cnt_w += 1

    origin = ['BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB']
    for a in range(8):
        for b in range(8):
            if origin[a][b] != board[i+a][j+b]:
                cnt_b += 1
    return min(cnt_b, cnt_w)
            
n, m = [int(_) for _ in input().split()]
board = [input() for _ in range(n)]

answer = 64
for i in range(n-7):
    for j in range(m-7):
        answer = min(answer, min_square(i,j))

print(answer)