from sys import stdin
input = stdin.readline

n, s, m = [int(x) for x in input().rstrip().split()]
v = [int(x) for x in input().rstrip().split()]
dp = [0 for _ in range(n)]

answer = -1

def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
    
@memo
def dfs(i, curvol):
    global answer
    if i == n:
        if answer < curvol:
            answer = curvol
        return
    if curvol+v[i] <= m:
        dfs(i+1, curvol+v[i])
    if curvol-v[i] >= 0:
        dfs(i+1, curvol-v[i])

dfs(0, s)
print(answer)