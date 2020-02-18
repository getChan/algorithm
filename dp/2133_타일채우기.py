n = int(input())

# dp[i] : 3Xi타일 채우는 경우의 수
# dp[0], dp[1] = 0
# dp[2] = 3
# dp[3] = 0
# dp[4] = 3*dp[2] + 2
# dp[5] = 0
# dp[6] = 3*dp[4] + 2
# dp[i] = 3*dp[i-2] + 2
dp = [0 for _ in range(n+1)]
dp[2] = 3
for i in range(4, n+1, 2):
    dp[i] = 3*dp[i-2] + 2
print(dp[n])