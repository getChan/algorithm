from sys import stdin
input = stdin.readline

t, w = [int(x) for x in input().rstrip().split()]
drop = []
for _ in range(t):
    times.append(t-1)
# dp[i][j] : i초에 j번 움직였을 때 자두의 최댓값
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1)
# dp[0][0] = times[0]
dp = [[0 for __ in range(w)] for _ in range(t)]

for i in range(t):
    for j in range(i):
        if drop[i] == 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1)
        else:
