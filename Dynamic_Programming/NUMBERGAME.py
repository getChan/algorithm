from sys import stdin
read = stdin.readline

def memoization(func):
    from collections import defaultdict
    memo = defaultdict(dict)
    def wrapper(a, b):
        if a in memo:
            if b in memo[a]:
                return memo[a][b]
        memo[a][b] = func(a,b)
        return memo[a][b]
    return wrapper


@memoization
def play(left, right):
    # 기저 사례
    if left > right:
        return 0

    ret = max(numbers[left]-play(left+1, right), numbers[right]-play(left, right-1))
    if right-left+1 >= 2:
        ret = max(ret, -play(left+2, right))
        ret = max(ret, -play(left, right-2))
        
    return ret

c = int(read().rstrip())
for _ in range(c):
    n = int(read().rstrip())
    numbers = [int(x) for x in read().rstrip().split()]
    print(play(0, len(numbers)-1))
    
