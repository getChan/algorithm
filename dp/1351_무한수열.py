n, p, q = [int(_) for _ in input().split()]
def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memo
def dfs(i, p, q):
    if i == 0:
        return 1
    return dfs(i//p, p, q) + dfs(i//q, p, q)

print(dfs(n, p, q))