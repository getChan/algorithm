# dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])) + 1
# if arr[i][j]
from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
dp = []
for _ in range(n):
    dp.append([int(x) for x in input().rstrip()])

answer = 0
for i in dp[0]:
    if i:
        answer = 1
        break
else:
    for i in range(n):
        if dp[i][0]:
            answer =1
            break

for i in range(1, n):
    for j in range(1, m):
        if dp[i][j]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            answer = max(dp[i][j], answer)
print(answer**2)