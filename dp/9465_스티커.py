from sys import stdin
input = stdin.readline
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    stickers = []
    stickers.append([int(x) for x in input().rstrip().split()])
    stickers.append([int(x) for x in input().rstrip().split()])

    dp = [[0 for __ in range(n)] for _ in range(2)]
    # dp[0][i] : 0번째 행, i번째 열 스티커까지의 최대값
    # dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
    # dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]
    
    for i in range(n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))