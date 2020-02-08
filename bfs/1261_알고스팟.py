# (N, M)까지 이동할 때 최소로 벽을 부수는 경우 찾기
# 1. 빈 방은 자유롭게 이동 가능
# 2. 벽은 부숴야만 이동 가능
# 2-1. 벽을 부수면 빈 방이 된다
# 3. 상하좌우로만 이동 가능

## 다익스트라로 풀어보자
# (1,1) 을 시작정점으로 두고
# 인접 정점 순회시마다 dist 배열 업데이트

from sys import stdin
import heapq

input = stdin.readline
m, n =[int(_) for _ in input().rstrip().split()]
maze = []
for _ in range(n):
    maze.append([int(x) for x in input().rstrip()])
MAX_DIST = 200
dist = [[MAX_DIST for _ in range(m)] for __ in range(n)]
dist[0][0] = 0
pq = [(0, (0, 0))]

while pq:
    w, u = heapq.heappop(pq)
    ui, uj = u
    if ui == n-1 and uj == m-1:
        print(dist[n-1][m-1])
        break
    if w > dist[ui][uj]: # 큐에 넣었던 경로보다 더 짧은 경로로 업데이트되었을 때
        continue
    for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        vi, vj = ui+di, uj+dj
        if not (0<=vi<n and 0<=vj<m):
            continue
        if maze[vi][vj]: # 벽이 있으면
            if dist[ui][uj]+1 < dist[vi][vj]:
                dist[vi][vj] = dist[ui][uj]+1
                heapq.heappush(pq, (dist[vi][vj], (vi, vj)))
        else: # 벽이 없으면
            if dist[ui][uj] < dist[vi][vj]:
                dist[vi][vj] = dist[ui][uj]
                heapq.heappush(pq, (dist[vi][vj], (vi, vj)))