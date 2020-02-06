n = int(input())
arr = [int(x) for x in input().split()]
dp = [1 for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1
    if dp[i] > answer:
        answer = dp[i]
print(answer)