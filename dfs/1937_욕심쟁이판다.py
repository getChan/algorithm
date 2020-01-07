from sys import stdin, setrecursionlimit
setrecursionlimit(500**2+2)
input = stdin.readline
# 메모이제이션 적용한 DFS로 풀어보자 (n*n)
n = int(input().rstrip())
bamboo = []
for _ in range(n):
    bamboo.append([int(x) for x in input().rstrip().split()])
visited = {}
def dfs(x, y):
    global bamboo, visited, n
    if (x,y) not in visited:
        tmp = [0]
        if x-1>=0 and bamboo[y][x-1] > bamboo[y][x]:
            tmp.append(dfs(x-1, y))
        if x+1<n and bamboo[y][x+1] > bamboo[y][x]:
            tmp.append(dfs(x+1, y))
        if y-1>=0 and bamboo[y-1][x] > bamboo[y][x]:
            tmp.append(dfs(x, y-1))
        if y+1<n and bamboo[y+1][x] > bamboo[y][x]:
            tmp.append(dfs(x, y+1))
    
        visited[(x,y)] = max(tmp)+1

    return visited[(x,y)]


for y in range(n):
    for x in range(n):
        if (x,y) not in visited:
            dfs(x, y)
            
print(max(visited.values()))