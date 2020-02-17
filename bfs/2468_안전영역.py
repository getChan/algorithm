from sys import stdin
from collections import deque
input = stdin.readline

n = int(input().rstrip())
arr = []
height = 0
for _ in range(n):
    arr.append([int(x) for x in input().rstrip().split()])
    height = max(arr[-1])


def bfs(i, j, level):
    queue = deque([(i, j)])
    while queue:
        i, j = queue.pop()
        for di, dj in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            if not (0 <= i+di < n and 0 <= j+dj < n):
                continue
            if arr[i+di][j+dj] > level and not visited[i+di][j+dj]:
                visited[i+di][j+dj] = True
                queue.append((i+di, j+dj))


answer = 1
for level in range(1, height):
    visited = [[False for _ in range(n)] for __ in range(n)]
    safety = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > level:
                safety += 1
                bfs(i, j, level)
    answer = max(answer, safety)
print(answer)
