from sys import stdin
read = stdin.readline

def memoization(func):
    from collections import defaultdict
    memo = defaultdict(dict)
    def wrapper(i):
        if i in memo:
            if 
            return memo[i]
        memo[i] = func(i)
        return memo[i]
    return wrapper

@memoization
def play(left, right):
    return max((numbers[left]-play(left+1, right)), numbers[right]-play(left, right-1),
    -play(left+2, right), -play(left, right-2))




c = int(read().rstrip())
for _ in range(c):
    n = int(read().rstrip())
    numbers = [int(x) for x in read().rstrip().split()]

