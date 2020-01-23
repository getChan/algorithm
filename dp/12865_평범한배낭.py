from sys import stdin
input = stdin.readline

n, k = [int(_) for _ in input().rstrip().split()]
obj = [0]*(k+1)
for _ in range(n):
    w, v = [int(_) for _ in input().rstrip().split()]
    if obj[w] >= v:
        pass
    else:
        obj[w] = v
# dp[w] : 현재 무게 w일때 최대 가치합
# dp[w] = max(obj[w], dp[w-1]+dp[1], ..., dp[(w+1)//2]+dp[w//2])
# dp[0] = 0
# dp[1] = obj[1]
# dp[2] = max(obj[2], dp[1]+dp[1])
dp = [0]*(k+1)
for i in range(1, k+1):
    maximum = obj[i]
    for j in range(1, (i//2)+1):
        if dp[i-j]+dp[j] > maximum:
            maximum = dp[i-j]+dp[j]
    dp[i] = maximum
print(dp[:k+1])