from sys import stdin
from collections import deque
input = stdin.readline

n = int(input().rstrip())
ocean = []
for _ in range(n):
    ocean.append([int(x) for x in input().rstrip().split()])

for i in range(n):
    for j in range(n):
        if ocean[i][j]==9:
            si, sj = i, j

def bfs(si, sj, size):
    global answer
    # print(si, sj)
    visited = {(si, sj)}
    queue = deque([(si, sj)])
    time = 0
    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            if 0 < ocean[i][j] < size:
                print(i, j, time)
                ocean[i][j] = 0
                answer += time
                return (i, j)
            for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                if 0<=i+di<n and 0<=j+dj<n and \
                    ocean[i+di][j+dj] <= size and (i+di, j+dj) not in visited:
                    visited.add((i+di, j+dj))
                    queue.append((i+di, j+dj))
        time += 1
    return False


answer = 0 # 모든 bfs시간의 합
size = 2
size_cnt = size
ocean[si][sj] = 0
next_pos = bfs(si, sj, size)
size_cnt -= 1
while next_pos:
    if size_cnt == 0:
        size += 1
        size_cnt = size
    next_pos = bfs(*next_pos, size)
    size_cnt -= 1
    
print(answer)