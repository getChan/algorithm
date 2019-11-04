from collections import deque
from sys import stdin

input = stdin.readline

def visited(m,n):
    global box
    if box[m][n] == 1 or box[m][n] == -1:
        return True
    else:
        return False

def push(idx):
    global box
    global queue
    m, n = idx
    
    if m+1 < len(box) and not visited(*(m+1, n)): 
        box[m+1][n] = 1
        queue.append((m+1, n))
    if m-1 >= 0 and not visited(*(m-1, n)): 
        box[m-1][n] = 1
        queue.append((m-1, n))
    if n+1 < len(box[0]) and not visited(*(m, n+1)): 
        box[m][n+1] = 1
        queue.append((m, n+1))
    if n-1 >= 0 and not visited(*(m, n-1)): 
        box[m][n-1] = 1
        queue.append((m, n-1))

    return queue

def is_zero():
    global box
    for row in box:
        for item in row:
            if item == 0:
                return True
                

m, n = [int(_) for _ in input().rstrip().split()]

box = [[int(x) for x in input().rstrip().split()] for _ in range(n)]

queue = deque()

# 큐 초기화
all_one = True
for m, row in enumerate(box):
    for n, tomato in enumerate(row):
        if tomato == 1:
            queue.append((m, n))
        if tomato == 0:
            all_one = False

level = 0
# 모두 익어 있으면
if all_one:
    print(level)

else:
    while queue:
        level += 1
        l = len(queue)
        for _ in range(l):
            idx = queue.popleft()
            queue = push(idx)

    if is_zero():
        print(-1)
    else:
        print(level-1)
