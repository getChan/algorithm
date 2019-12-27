from collections import defaultdict

n = int(input())
# dp[i] : i번 인덱스까지 연산 횟수의 최소값
dp = defaultdict(lambda:10**5)

def dfs(n, level, flag):
    global dp
    dp[n] = level
    if n == 1:
        return
    if n % 3 == 0 and dp[n//3] > level+1:
        dfs(n//3, level+1, 2)
    if n % 2 == 0 and dp[n//2] > level+1:
        dfs(n//2, level+1, 2)
    if flag and dp[n-1] > level+1:
        dfs(n-1, level+1, flag-1)

dfs(n, level=0, flag=2)# 2번까지 한칸씩 움직일 수 있다.
print(dp[1])