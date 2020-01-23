from sys import stdin

dp = [0 for _ in range(10000+1)]
dp[1], dp[2], dp[3] = 1, 2, 3, 4,

target = 10000
def dfs(num):
    if num > target:
        return
    if num == target:
        return 1
    if num%3
    dfs(num+1)
    dfs(num+2)
    dfs(num+3)

dfs(0)





for _ in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())        
    print(dp[n])