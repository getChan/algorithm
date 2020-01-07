from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, y, cabages):
    cabages[y][x] = 0
    queue = deque([(x,y)])
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x > 0 and cabages[y][x-1]:
                cabages[y][x-1] = 0
                queue.append((x-1,y))
            if x < len(cabages[0])-1 and cabages[y][x+1]:
                cabages[y][x+1] = 0
                queue.append((x+1, y))
            if y > 0 and cabages[y-1][x]:
                cabages[y-1][x] = 0
                queue.append((x, y-1))
            if y < len(cabages)-1 and cabages[y+1][x]:
                cabages[y+1][x] = 0
                queue.append((x, y+1))

t = int(input().rstrip())
for _ in range(t):
    m, n, k = [int(x) for x in input().rstrip().split()]
    cabages = [[0 for _ in range(m)] for __ in range(n)]
    for __ in range(k):
        x, y = [int(x) for x in input().rstrip().split()]
        cabages[y][x] = 1
    answer = 0
    for y in range(n):
        for x in range(m):
            if cabages[y][x] and (x,y):
                bfs(x, y, cabages)
                answer += 1
    print(answer)