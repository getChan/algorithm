n = int(input())
arr = [int(x) for x in input().split()]
# dp[i] : i번째 수까지 가장 긴 감소하는 부분 수열의 길이
dp = [1 for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(i):
        if arr[i] < arr[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
    if dp[i] > answer:
        answer = dp[i]

print(answer)