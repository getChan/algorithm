n = int(input())

# dp[i] : 길이가 i일 때 오르막 수의 개수
# dp[i][j] = sigma (j = 1 to 10) (dp[i-1][j]) - dp[i-1][j]
dp = [[1 for _ in range(10)] for _ in range(n)]
for i in range(1, n):
    dp[i][0] = sum(dp[i-1]) % 10007
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1]-dp[i-1][j-1]
print(sum(dp[-1])%10007)