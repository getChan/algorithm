from collections import deque
from sys import stdin
input = stdin.readline

mapp = []
n, m = [int(x) for x in input().rstrip().split()]
for _ in range(n):
    mapp.append([int(x) for x in input().rstrip()])
visited = set()
queue = deque([(0, 0, False)]) # (i, j, isbreak)
visited.add((0,0,False))
time = 1
while queue:
    for _ in range(len(queue)):
        i, j, isbreak = queue.popleft()
        if (i, j) == (n-1, m-1):
            print(time)
            queue = None
            break

        for di, dj in [(0,-1), (-1,0), (0,1), (1,0)]:
            if not (0<=i+di<n and 0<=j+dj<m):
                continue
            if isbreak:
                if (i+di, j+dj, True) not in visited and\
                    not mapp[i+di][j+dj]:
                    visited.add((i+di, j+dj, True))
                    queue.append((i+di, j+dj, True))
            else:
                if (i+di, j+dj, bool(mapp[i+di][j+dj])) not in visited:
                    visited.add((i+di, j+dj, bool(mapp[i+di][j+dj])))
                    queue.append((i+di, j+dj, bool(mapp[i+di][j+dj])))
    time += 1
if not queue==None:
    print(-1)