from sys import stdin
import heapq
input = stdin.readline

n = int(input().rstrip())
ocean = []
for _ in range(n):
    ocean.append([int(x) for x in input().rstrip().split()])

for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            si, sj = i, j
            ocean[i][j] = 0  # 시작 위치 0으로


def bfs(si, sj, size):
    """
    물고기를 찾아 먹는다.
    """
    time = 0
    queue = [(time, si, sj)]
    visited = {(si, sj)}
    while queue:
        for _ in range(len(queue)):
            time, i, j = heapq.heappop(queue)
            if 0 < ocean[i][j] < size:  # 먹을 수 있다
                ocean[i][j] = 0
                return i, j, time

            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if not (0 <= i+di < n and 0 <= j+dj < n):
                    continue
                if ocean[i+di][j+dj] <= size \
                        and (i+di, j+dj) not in visited:  # 자기보다 크면 지날 수 없다.
                    visited.add((i+di, j+dj))
                    heapq.heappush(queue, (time+1, i+di, j+dj))
        time += 1
    return si, sj, 0  # 종료 조건, 움직이지 않은 상태


answer = 0
size = 2
eaten = 0
while True:
    si, sj, time = bfs(si, sj, size)
    if time == 0:
        break
    answer += time
    eaten += 1
    if eaten == size:
        size += 1
        eaten = 0
print(answer)