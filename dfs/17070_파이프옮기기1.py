from sys import stdin
input = stdin.readline
n = int(input().rstrip())
house = []
for _ in range(n):
    house.append([int(x) for x in input().rstrip().split()])
def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

scratch = lambda r, c: house[r][c] or house[r-1][c] or house[r][c-1]
@memo
def dfs(r, c, way):
    '''
    way - 0 : 가로, 1 : 세로, 2, 대각선 
    '''
    if r == n-1 and c == n-1:
        return 1

    result = 0
        
    if way==0:
        if c+1 < n :
            if not house[r][c+1]:
                result += dfs(r, c+1, 0)
            if r+1 < n and not scratch(r+1, c+1):
                result += dfs(r+1, c+1, 2)
        
    if way==1:
        if r+1 < n:
            if not house[r+1][c]:
                result += dfs(r+1, c, 1)
            if c+1 < n and not scratch(r+1, c+1):
                result += dfs(r+1, c+1, 2)
        
    if way==2:
        if c+1 < n and not house[r][c+1]:
            result += dfs(r, c+1, 0)
        if r+1 < n and not house[r+1][c]:
            result += dfs(r+1, c, 1)
        if r+1 < n and c+1 < n and not scratch(r+1, c+1):
            result += dfs(r+1, c+1, 2)    
    
    return result

print(dfs(0, 1, 0))
