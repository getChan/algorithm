n, k = (int(_) for _ in input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# dp[i] : 가치의 합이 i인 경우의 수
dp = [0 for i in range(k+1)]
for coin in coins:
    dp[coin] = 1
coins.sort()
start = coins[0]
if k < start:
    print(0)
else:
    for i in range(start+1, k+1):
        print(dp)
        tmp = dp[i]
        for coin in coins:
            if i-coin < start:
                break
            tmp += dp[i-coin]
        dp[i] = tmp
        