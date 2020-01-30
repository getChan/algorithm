from sys import setrecursionlimit
setrecursionlimit(1000*1000+2)
n = int(input())
game = []
for _ in range(n):
    game.append([int(__) for __ in input().split()])

def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memo
def dfs(i, j):
    if i==n-1 and j==n-1:
        return 1
    if i >= n or j >= n or not game[i][j]:
        return 0
    
    return dfs(i+game[i][j], j) + dfs(i, j+game[i][j])
    
print(dfs(0, 0))