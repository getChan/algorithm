n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
cnt = 1
buffer = 1
for i in range(4, n+1):
    if 2*dp[i-3] >= dp[i-1]+buffer:
        buffer = dp[i-3]
        dp[i] = dp[i-3]+buffer
    else:
        dp[i] = dp[i-1]+buffer

print(dp)
print(dp[n])