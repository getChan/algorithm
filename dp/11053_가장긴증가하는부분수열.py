n = int(input())
a = [int(x) for x in input().split()]

# dp[i] : i번째 수까지 LIS
dp = [1 for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
    if dp[i] > answer:
        answer = dp[i]
print(dp)
print(answer)