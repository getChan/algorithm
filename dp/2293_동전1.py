n, k = (int(_) for _ in input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
cnt = 0
coins.sort()

# case[i, sum] = i번째 동전만 가지고 sum을 만들 수 있는 경우의 수
# dp[n] = case[i+1] + case[i] + ... + case[n]
for i in range(coins):
    if k%coins[i] == 0:
        cnt += 1