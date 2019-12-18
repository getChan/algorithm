from collections import deque
n = int(input())
paint1, paint2 = [], []
for _ in range(n):
    tmp1 = []
    tmp2 = []
    for c in input():
        tmp1.append(c)
        if c == 'G':
            tmp2.append('R')
        else:
            tmp2.append(c)
    paint1.append(tmp1)
    paint2.append(tmp2)
            
visited = [[False for _ in range(n)] for __ in range(n)]
cnt1, cnt2 = 0, 0
queue = deque()
for ii in range(n):
    for jj in range(n):
        if visited[ii][jj]:
            continue
        else:
            cnt1 += 1
            queue.append((ii, jj))
            while queue:
                i, j = queue.popleft()
                color = paint1[i][j]

                if i and paint1[i-1][j] == color:
                    if not visited[i-1][j]:
                        visited[i-1][j] = True
                        queue.append((i-1, j))
                if i < n-1 and paint1[i+1][j] == color:
                    if not visited[i+1][j]:
                        visited[i+1][j] = True
                        queue.append((i+1, j))
                if j and paint1[i][j-1] == color:
                    if not visited[i][j-1]:
                        visited[i][j-1] = True
                        queue.append((i, j-1))
                if j < n-1 and paint1[i][j+1] == color:
                    if not visited[i][j+1]:
                        visited[i][j+1] = True
                        queue.append((i, j+1))

visited = [[False for _ in range(n)] for __ in range(n)]
for ii in range(n):
    for jj in range(n):
        if visited[ii][jj]:
            continue
        else:
            cnt2 += 1
            queue.append((ii, jj))
            while queue:
                i, j = queue.popleft()
                color = paint2[i][j]

                if i and paint2[i-1][j] == color:
                    if not visited[i-1][j]:
                        visited[i-1][j] = True
                        queue.append((i-1, j))
                if i < n-1 and paint2[i+1][j] == color:
                    if not visited[i+1][j]:
                        visited[i+1][j] = True
                        queue.append((i+1, j))
                if j and paint2[i][j-1] == color:
                    if not visited[i][j-1]:
                        visited[i][j-1] = True
                        queue.append((i, j-1))
                if j < n-1 and paint2[i][j+1] == color:
                    if not visited[i][j+1]:
                        visited[i][j+1] = True
                        queue.append((i, j+1))


print(cnt1, cnt2)