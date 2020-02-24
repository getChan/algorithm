from sys import stdin
from itertools import combinations
from collections import deque
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
maps = []  # 연구실 배열
for _ in range(n):
    maps.append([int(x) for x in input().rstrip().split()])

viruses = []  # 바이러스를 놓을 수 있는 위치
cnt = 0  # 빈 칸의 수
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            viruses.append((i, j))
        elif maps[i][j] == 0:
            cnt += 1
MAX_NUM = 2500  # 최대 시간


def bfs(select):
    blank = 0  # 방문한 빈칸의 수
    visited = [[False]*n for _ in range(n)]
    for s in select:
        visited[s[0]][s[1]] = True
    queue = deque(select)
    time = 0
    while queue:
        if blank >= cnt:  # 모든 빈칸 전염시켰으면
            break
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if not (0 <= i+di < n and 0 <= j+dj < n):
                    continue
                if maps[i+di][j+dj] != 1 and not visited[i+di][j+dj]:
                    if maps[i+di][j+dj] == 0:
                        blank += 1  # 다음 방문이 빈칸이면 방문한 빈칸의 수 증가
                    queue.append((i+di, j+dj))
                    visited[i+di][j+dj] = True
        time += 1
    else:  # 전염 불가능
        return MAX_NUM
    return time


answer = MAX_NUM
for select in combinations(viruses, m):
    answer = min(answer, bfs(select))
if answer == MAX_NUM:
    print(-1)
else:
    print(answer)
