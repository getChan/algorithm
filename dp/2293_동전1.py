n, k = (int(_) for _ in input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

# dp[i] : 가치의 합이 i인 경우의 수
dp = [i for i in range(k+1)]

for i in range(n):
    for j in range(k)
