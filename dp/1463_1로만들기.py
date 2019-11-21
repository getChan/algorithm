# List[N] = min(List[N//3], List[N//2], List[N-1]) + 1
n = int(input())
dp = [0,0,1,1]

for i in range(4,n+1):
    dp.append(dp[i-1]+1)

    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])
