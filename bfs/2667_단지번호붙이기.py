from pprint import pprint
from collections import deque
n = int(input())
apart = []
for _ in range(n):
    apart.append(list(input()))

def bfs(i,j):
    global apart
    queue = deque()
    apart[i][j] = '0'
    queue.append((i, j))
    num = 1
    while queue:
        i, j = queue.popleft()
        if j-1>=0 and apart[i][j-1] == '1':
            apart[i][j-1] = '0'
            queue.append((i,j-1))
            num += 1
        if i-1>=0 and apart[i-1][j] == '1':
            apart[i-1][j] = '0'
            queue.append((i-1,j))
            num += 1
        if j+1<n and apart[i][j+1] == '1':
            apart[i][j+1] = '0'
            queue.append((i,j+1))
            num += 1
        if i+1<n and apart[i+1][j] == '1':
            apart[i+1][j] = '0'
            queue.append((i+1,j))
            num += 1
    return num

cnt = 0
i = 0
houses = []
while i < n:
    j = 0
    while j < n:
        if apart[i][j] == '1':
            houses.append(bfs(i,j))
            cnt += 1
        j += 1
    i += 1
print(cnt)
for h in sorted(houses):
    print(h)