from sys import setrecursionlimit, stdin
from collections import deque
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
maze = []
for _ in range(n):
    maze.append([int(x) for x in input().rstrip()])
visited = [[100*100 for _ in range(m)] for __ in range(n)]
queue = deque([(0,0)])
cnt = 1
visited[0][0] = cnt
while queue:
    cnt += 1
    for _ in range(len(queue)):
        i, j = queue.popleft()
        if i>0 and maze[i-1][j]:
            if visited[i-1][j] > cnt:
                visited[i-1][j] = cnt
                queue.append((i-1, j))
        if j>0 and maze[i][j-1]:
            if visited[i][j-1] > cnt:
                visited[i][j-1] = cnt
                queue.append((i, j-1))
        if i<n-1 and maze[i+1][j]:
            if visited[i+1][j] > cnt:
                visited[i+1][j] = cnt
                queue.append((i+1, j))
        if j<m-1 and maze[i][j+1]:
            if visited[i][j+1] > cnt:
                visited[i][j+1] = cnt
                queue.append((i, j+1))
print(visited[n-1][m-1])


# setrecursionlimit(100*100)
# visited = [[100*100 for _ in range(m)] for __ in range(n)]
# def dfs(maze, visited, i, j, cnt):
#     visited[i][j] = cnt

#     if i==n-1 and j==m-1:
#         return

#     if i>0 and maze[i-1][j]:
#         if visited[i-1][j] > cnt+1:
#             dfs(maze, visited, i-1, j, cnt+1)
#     if j>0 and maze[i][j-1]:
#         if visited[i][j-1] > cnt+1:
#             dfs(maze, visited, i, j-1, cnt+1)
#     if i<n-1 and maze[i+1][j]:
#         if visited[i+1][j] > cnt+1:
#             dfs(maze, visited, i+1, j, cnt+1)
#     if j<m-1 and maze[i][j+1]:
#         if visited[i][j+1] > cnt+1:
#             dfs(maze, visited, i, j+1, cnt+1)
#     return

# dfs(maze, visited, 0, 0, cnt=1)
# print(visited[n-1][m-1])

