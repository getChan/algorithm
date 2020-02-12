# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값 구하기
# - 4^5개 경우의 수. 완탐으로 가능
from sys import stdin
from copy import deepcopy
input = stdin.readline

n = int(input().rstrip())
board = []
for _ in range(n):
    board.append([int(x) for x in input().rstrip().split()])

def up(board, level):
    added = set()
    for _ in range(n-1):
        for i in range(n-1):
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] += board[i+1][j]
                    board[i+1][j] = 0
                elif board[i][j] == board[i+1][j] and\
                    (i, j) not in added and (i+1, j) not in added:
                    added.add((i,j))
                    board[i][j] += board[i+1][j]
                    board[i+1][j] = 0
    recur(board, level+1)
                
def down(board, level):
    added = set()
    for _ in range(n-1):
        for i in range(n-1, 0, -1):
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] += board[i-1][j]
                    board[i-1][j] = 0
                elif board[i][j] == board[i-1][j] and\
                    (i, j) not in added and (i-1, j) not in added:
                    added.add((i,j))
                    board[i][j] += board[i-1][j]
                    board[i-1][j] = 0
    recur(board, level+1)

def left(board, level):
    added = set()
    for _ in range(n-1):
        for j in range(n-1):
            for i in range(n):
                if board[i][j] == 0:
                    board[i][j] += board[i][j+1]
                    board[i][j+1] = 0
                elif board[i][j] == board[i][j+1] and\
                    (i, j) not in added and (i, j+1) not in added:
                    added.add((i,j))
                    board[i][j] += board[i][j+1]
                    board[i][j+1] = 0
    recur(board, level+1)
                
def right(board, level):
    added = set()
    for _ in range(n-1):
        for j in range(n-1, 0, -1):
            for i in range(n):
                if board[i][j] == 0:
                    board[i][j] += board[i][j-1]
                    board[i][j-1] = 0
                elif board[i][j] == board[i][j-1] and\
                    (i, j) not in added and (i, j-1) not in added:
                    added.add((i,j))
                    board[i][j] += board[i][j-1]
                    board[i][j-1] = 0
    recur(board, level+1)

# def memo(func):
#     cache = {}
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#     return wrapper

answer = 0
def recur(board, level):
    global answer
    if level > 5:
        localamax = max(map(max, board))
        if localamax > answer:
            answer = localamax
        return
    for move in (left, right, up, down):
        move(deepcopy(board), level)

recur(board, 1)
print(answer)