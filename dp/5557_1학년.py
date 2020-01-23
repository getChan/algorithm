n = int(input())
num = [int(_) for _ in input().split()]

def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memo
def solve(idx, cursum):
    if not (0<= cursum <= 20):
        return 0
    if idx == n-2:
        if cursum == num[n-1]:
            return 1
        else:
            return 0
    value = 0
    value += solve(idx+1, cursum+num[idx+1])
    value += solve(idx+1, cursum-num[idx+1])
    return value

print(solve(0, num[0]))