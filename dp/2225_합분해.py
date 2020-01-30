n, k = [int(_) for _ in input().split()]

dp = [[0 for _ in range(k+1)] for __ in range(n+1)]
for i in range(n+1):
    dp[i][1] = 1

for i in range(1, k+1):
    for j in range(n+1):
        for l in range(j+1):
            dp[j][i] += dp[j-l][i-1] % 1000000000

print(dp[n][k]%1000000000)