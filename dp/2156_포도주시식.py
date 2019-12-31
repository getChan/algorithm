from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
input = stdin.readline
n = int(input().rstrip())
wines = []
for _ in range(n):
    wines.append(int(input().rstrip()))

# dp[before][now] : 이전에 before 마시고 현재 now 마셨을 때 최댓값
# dp[before][now] = 
# max(dp[before-1][before], dp[befroe-2][before]) + wines[now]
dp = [[0 for _ in range(n)] for __ in range(n)]
dp[0][0] = wines[0]
dp[1][1] = wines[1]
dp[2] = 