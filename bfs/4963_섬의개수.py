from collections import deque
while True:
    w, h = [int(x) for x in input().split()]
    if not (w or h):
        break
    mapp = []
    start = []
    for i in range(h):
        row = []
        for j, v in enumerate(input().split()):
            if int(v):
                start.append((i, j))
            row.append(int(v))
        mapp.append(row)

    answer = 0
    visited = set()
    for s in start:
        if s not in visited:
            answer += 1
            queue = deque([s])
            while queue:
                i, j = queue.popleft()
                for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if 0<=i+di<h and 0<=j+dj<w and (i+di, j+dj) not in visited and mapp[i+di][j+dj]:
                        visited.add((i+di, j+dj))
                        queue.append((i+di, j+dj))
    
    print(answer)