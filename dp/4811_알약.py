from sys import stdin
input = stdin.readline

dp = [[0 for _ in range(62)] for __ in range(31)]
# dp[w][h] = w개, h개씩 가지고 있을 떄 경우의 수
def pills():
    for w in range(31):
        for h in range(61):
            if w == 0:
                dp[w][h] = 1
            elif h == 0:
                dp[w][h] = dp[w-1][h+1]
            else:
                dp[w][h] = dp[w-1][h+1] + dp[w][h-1]
            # print(w, h, dp[w][h])

pills()
while True:
    n = int(input().rstrip())
    
    if not n:
        break
    print(dp[n][0])