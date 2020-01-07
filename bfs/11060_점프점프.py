from collections import deque

n = int(input())
maze = [int(x) for x in input().split()]


################# BFS ##################
# visitied = [False for _ in range(n)]

# jump = 0 # 점프수
# flag = False # 끝에 도달하면 True

# visitied[0] = True
# queue = deque([0]) # 현재 위치

# while queue and not flag:
#     for _ in range(len(queue)):
#         pos = queue.popleft()
#         if pos >= n-1:
#             flag = True
#             break
#         for i in range(maze[pos], 0, -1):
#             if pos+i < n and not visitied[pos+i]:
#                 visitied[pos+i] = True
#                 queue.append(pos+i)
#     jump += 1

# if not flag:
#     print(-1)
# else:
#     print(jump-1)


################# DP ##################
# dp[i] : i번째 칸까지 가는 최소 점프
# dp[n] = 