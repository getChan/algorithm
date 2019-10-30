from collections import deque
from sys import stdin

input = stdin.readline

def visited(idx):
    global box
    m, n, h = idx
    if box[m][n][h] == 1 or box[m][n][h] == -1:
        return True
    else:
        return False
def push(idx):
    global box
    global queue
    m, n, h = idx
    
    if m+1 < len(box) and not visited((m+1, n, h)): 
        box[m+1][n][h] = 1
        queue.append((m+1, n, h))
    if m-1 >= 0 and not visited((m-1, n, h)): 
        box[m-1][n][h] = 1
        queue.append((m-1, n, h))
    if n+1 < len(box[0]) and not visited((m, n+1, h)): 
        box[m][n+1][h] = 1
        queue.append((m, n+1, h))
    if n-1 >= 0 and not visited((m, n-1, h)): 
        box[m][n-1][h] = 1
        queue.append((m, n-1, h))
    if h+1 < len(box[0][0]) and not visited((m, n, h+1)): 
        box[m][n][h+1] = 1
        queue.append((m, n, h+1))
    if h-1 >= 0 and not visited((m, n, h-1)): 
        box[m][n][h-1] = 1
        queue.append((m, n, h-1))

    return queue

m, n, h = [int(_) for _ in input().rstrip().split()]

box = [[[int(x) for x in input().rstrip().split()] for _ in range(n)] for __ in range(h)]

queue = deque()
flag = 0
for m, two in enumerate(box):
    for n, one in enumerate(two):
        for h, i in enumerate(one):
            if i == 1:
                queue.append((m, n, h))
            if i == 0:
                flag += 1

level = 0
if not flag:
    print(0)
else:
    while queue:
        level += 1
        l = len(queue)
        for _ in range(l):
            idx = queue.popleft()
            queue = push(idx)

    flag = True
    for two in box:
        if not flag : break
        for one in two:
                if not flag: break
                for i in one:
                        if int(i) == 0:
                            print(-1)
                            flag = False
                            break
    if flag:
        print(level-1)


