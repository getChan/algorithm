# 최단 경로를 구하는 문제
# DP이용한 DFS로 풀어보자
# from collections import deque
# def dfs(i, j, cursum):
#     global arr, dp
#     l = len(arr)-1
#     if i>l or j>l:
#         return
#     if dp[i][j] > arr[i][j]+cursum:
#         dp[i][j] = arr[i][j]+cursum
#         dfs(i+1,j,dp[i][j])
#         dfs(i,j+1,dp[i][j])
#     else:
#         return
# c = 0
# while True:
#     c += 1
#     n = int(input())
#     MAXNUM = 9*n*n
#     if not n:
#         break
#     arr = []
#     for _ in range(n):
#         arr.append([int(x) for x in input().split()])
#     dp = [[MAXNUM for _ in range(n)] for __ in range(n)]
#     dfs(0, 0, 0)
#     print('Problem {}: {}'.format(c, dp[n-1][n-1]))


# 실패했다. 최단 경로는 인접한 오른쪽, 아래칸을 지나치치 않을 수도 있다.
from sys import stdin
import heapq
def dijkstra(arr, dist, n):
    pq = []
    heapq.heappush(pq, (arr[0][0],0,0))
    while pq:
        v, i, j = heapq.heappop(pq)
        if dist[i][j] < v:
            continue
        if i-1>=0:
            if dist[i-1][j] > v+arr[i-1][j]:
                dist[i-1][j] = v+arr[i-1][j]
                heapq.heappush(pq, (dist[i-1][j], i-1, j))
        if i+1<n:
            if dist[i+1][j] > v+arr[i+1][j]:
                dist[i+1][j] = v+arr[i+1][j]
                heapq.heappush(pq, (dist[i+1][j], i+1, j))
        if j-1>=0:
            if dist[i][j-1] > v+arr[i][j-1]:
                dist[i][j-1] = v+arr[i][j-1]
                heapq.heappush(pq, (dist[i][j-1], i, j-1))
        if j+1<n:
            if dist[i][j+1] > v+arr[i][j+1]:
                dist[i][j+1] = v+arr[i][j+1]
                heapq.heappush(pq, (dist[i][j+1], i, j+1))
    return dist[n-1][n-1]
        

input = stdin.readline
c = 0
while True:
    c += 1
    n = int(input().rstrip())
    MAXNUM = 9*n*n
    if not n:
        break
    arr = []
    for _ in range(n):
        arr.append([int(x) for x in input().rstrip().split()])
    dist = [[MAXNUM for _ in range(n)] for __ in range(n)]
    print('Problem {}: {}'.format(c, dijkstra(arr, dist, n)))


# 시간 초과 난다...
# 우선순위 큐를 효율적으로 이용해야 한다.
# from heapq import heappush, heappop
# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write

# t = 0
# INF = 1e9
# dx = (-1, 0, 1, 0)
# dy = (0, 1, 0, -1)

# def dijkstra(n, a, dist):
#     pq = []
#     heappush(pq, (0, 0, 0))
#     dist[0][0] = 0
#     while pq:
#         d, x, y = heappop(pq)
#         if dist[x][y] < d:
#             continue
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             nd = d + a[nx][ny]
#             if dist[nx][ny] > nd:
#                 dist[nx][ny] = nd
#                 heappush(pq, (nd, nx, ny))
#     return dist[n-1][n-1] + a[0][0]

# while True:
#     t += 1
#     n = int(input())
#     if n is 0:
#         break
#     a = [list(map(int, input().split())) for _ in range(n)]
#     dist = [[INF]*n for _ in range(n)]
#     print("Problem %d: %d\n" % (t, dijkstra(n, a, dist)))


# 출처: https://rebas.kr/699 [PROJECT REBAS]