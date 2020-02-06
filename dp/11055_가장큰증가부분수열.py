n = int(input())
arr = [int(x) for x in input().split()]
dp = arr.copy()
answer = 0
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
    if answer < dp[i]:
        answer = dp[i]

print(answer)
# dp[i] : i를 마지막 항으로 증가하는 부분 수열 중 합이 가장 큰 값