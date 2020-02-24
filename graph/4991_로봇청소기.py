from sys import stdin
from collections import deque
input = stdin.readline

while True:
    w, h = [int(x) for x in input().rstrip().split()]
    if not w and not h:
        break
    room = []
    for _ in range(h):
        room.append([x for x in input().rstrip()])

    targets = []
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                s = (i, j)
                room[i][j] = '.'
            elif room[i][j] == '*':
                targets.append((i, j))

    def bfs(s):
        queue = deque([s])
        visited = {s}
        level = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if room[i][j] == '*':
                    room[i][j] = '.'
                    return level, (i, j)
                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if not (0 <= i+di < h and 0 <= j+dj < w):
                        continue
                    if room[i+di][j+dj] != 'x' and (i+di, j+dj) not in visited:
                        visited.add((i+di, j+dj))
                        queue.append((i+di, j+dj))
            level += 1
        return 0, 0

    answer = 0
    for _ in range(len(targets)):
        level, s = bfs(s)
        if not level:
            print(-1)
            break
        answer += level
    else:
        print(answer)
