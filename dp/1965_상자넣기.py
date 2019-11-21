n = int(input())
boxes = [int(_) for _ in input().split()]
dp = [1 for _ in range(n)]
# 최장증가수열 문제
# dp[i] : i에서 끝나는 최장증가수열
answer = 1
for i in range(0, n):
    for j in range(0, i):
        if boxes[i] > boxes[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
    if dp[i] > answer:
        answer = dp[i]
print(answer)