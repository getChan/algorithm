# from pprint import pprint
from sys import stdin
input = stdin.readline
n = int(input().rstrip())

answer = 0

def dfs(chess, row, col):
    global answer
    chess = list(map(list, chess))
    if row == n-1:
        answer += 1
        return
    l, r = col, col
    for i in range(row, n):
        chess[i][col] = 1
        if l >= 0:
            chess[i][l] = 1
            l -= 1
        if r < n:
            chess[i][r] = 1
            r += 1
    for j in range(n):
        chess[row][j] = 1
    # pprint(chess)
    chess = tuple(map(tuple, chess))
    for i in range(n):
        if not chess[row+1][i]:
            dfs(chess, row+1, i)
    return
chess = tuple(tuple(0 for _ in range(n)) for __ in range(n))
for i in range(n):
    dfs(chess, 0, i)

print(answer)
