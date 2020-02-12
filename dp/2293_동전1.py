n, k = (int(_) for _ in input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# dp[i] : 가치의 합이 i인 경우의 수
# dp[i] = dp[i-j], j:동전들 <- 중복을 제거하지 못함

dp = [0 for i in range(k+1)]

1111111111
111111112
