from sys import stdin
from collections import deque
input = stdin.readline

r, c = [int(_) for _ in input().rstrip().split()]
mapp = []
for _ in range(r):
    mapp.append([x for x in input().rstrip()])
gosum = deque()
visited = set()
water = deque()
for i in range(r):
    for j in range(c):
        if mapp[i][j] == 'S':
            mapp[i][j] = '.'
            gosum.append((i, j))
            visited.add((i, j))            
        if mapp[i][j] == '*':
            water.append((i, j))

def fill_water():
    for _ in range(len(water)):
        i, j = water.popleft()
        for di, dj in [(0,-1), (-1,0), (0,1), (1,0)]:
            if not (0<=i+di<r and 0<=j+dj<c):
                continue
            if mapp[i+di][j+dj] == '.':
                mapp[i+di][j+dj] = '*'
                water.append((i+di, j+dj))
time = 0
while gosum:
    fill_water()
    for _ in range(len(gosum)):
        i, j = gosum.popleft()
        if mapp[i][j] == 'D':
            print(time)
            gosum = None
            break
        for di, dj in [(0,-1), (-1,0), (0,1), (1,0)]:
            if not (0<=i+di<r and 0<=j+dj<c):
                continue
            if (i+di, j+dj) not in visited and\
                mapp[i+di][j+dj] in ('.', 'D'):
                visited.add((i+di, j+dj))
                gosum.append((i+di, j+dj))

    time += 1

if gosum != None:
    print('KAKTUS')