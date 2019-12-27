from sys import stdin
t = int(stdin.readline().rstrip())
# dp[i] : i일때 호출된 수
# dp[0] = (1, 0)
# dp[1] = (0, 1)
# dp[2] = dp[1]+dp[0] = (1, 1)
# dp[3] = dp[1]+dp[0]+dp[1] = (1, 2)
# dp[4] = dp[1]+dp[0]+dp[1]+dp[1]+dp[0] = (2, 3)
# dp[i+1] = dp[i]+dp[i-1]
dp = dict()
dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, 41):
        dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

for _ in range(t):
    n = int(stdin.readline().rstrip())
    print(dp[n][0], dp[n][1])