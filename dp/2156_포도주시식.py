from sys import stdin
input = stdin.readline

wines = []
for _ in range(int(input().rstrip())):
    wines.append(int(input().rstrip()))
# dp[i] : i번째 포도주까지 마실 때 최댓값
dp = [0 for _ in range(len(wines))]
# dp[0] = wines[0]
# dp[1] = dp[0]+wines[1]
# dp[2] = max(dp[0]+wines[2], dp[1])
# dp[3] = max(dp[1]+wines[3], dp[2])
# dp[4] = max(dp[2]+wines[4], dp[3])
dp[0] = wines[0]
dp[1] = dp[0]+wines[1]
for i in range(2, len(dp)):
    dp[i] = max(dp[i-2]+wines[i], dp[i-1])
print(dp)