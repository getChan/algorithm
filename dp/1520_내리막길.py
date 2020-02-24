from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(500*500)

m, n = [int(x) for x in input().rstrip().split()]
maps = []
for _ in range(m):
    maps.append([int(x) for x in input().rstrip().split()])


# DFS+DP로 풀어보자
def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@memo
def dfs(i, j):
    if (i, j) == (m-1, n-1):
        return 1
    cnt = 0
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if not (0 <= i+di < m and 0 <= j+dj < n):
            continue
        if maps[i+di][j+dj] < maps[i][j]:
            cnt += dfs(i+di, j+dj)
    return cnt


print(dfs(0, 0))