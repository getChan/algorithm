n = int(input())
# dp[n] = max(starir[n]+dp[n-1], stair[n]+dp[n-2])
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))
def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
@memo
def dfs(n, one_step=False):
    global stairs
    if n < 1:
        return 0
    if one_step:
        return stairs[n]+dfs(n-2)
    else:
        return max(stairs[n]+dfs(n-1, True), stairs[n]+dfs(n-2))

print(dfs(n))