from sys import stdin
input = stdin.readline

n, m = [int(_) for _ in input().rstrip().split()]
maze = [[0 for _ in range(m+1)]]
for _ in range(n):
    maze.append([0]+[int(x) for x in input().rstrip().split()])

# dp[n][m] : (n, m)에서 사탕 개수의 최댓값
# dp[n][m] = max(dp[n-1][m], dp[n][m-1], dp[n-1][m-1]) + maze[n][m]
dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
dp[1][1] = maze[1][1]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i][j]
print(dp[n][m])
