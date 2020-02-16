n = int(input())
p = [int(x) for x in input().split()]

p.insert(0, 0) # 인덱스 맞춰주기 위함
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i] = max([dp[j]+p[i-j] for j in range(i)])
print(dp[n])
