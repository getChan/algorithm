from sys import stdin
input = stdin.readline
dp = [1 for _ in range(101)]
dp[4], dp[5] = 2, 2
for i in range(6, 101):
    dp[i] = dp[i-5]+dp[i-1]

for t in range(int(input().rstrip())):
    print(dp[int(input().rstrip())])