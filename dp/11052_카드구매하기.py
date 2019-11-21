import sys

n = int(input())
sys.setrecursionlimit(n**n)
p = [0]
p.extend([int(_) for _ in input().split()])
answer = 0
def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
@memo
def dfs(i, price):
    global n, p, answer
    if i > n:
        return
    if i == n:
        if price > answer:
            answer = price 
    for j in range(1, n+1):
        dfs(i+j, price+p[j])
    
for i in range(1, n+1):
    dfs(i, p[i])

print(answer)
