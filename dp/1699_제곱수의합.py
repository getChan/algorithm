from sys import setrecursionlimit
setrecursionlimit(100000)
n = int(input())

def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memo 
def dp(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if not i**(1/2)% 1 : # i를 하나의 제곱수 항으로 표현 가능하면
        return 1
    sqrt = [x**2 for x in range(int((i//2)**(1/2)), int(i**(1/2)+1))]
    return min(map(lambda x: dp(x)+dp(i-x), sqrt))

print(dp(n))