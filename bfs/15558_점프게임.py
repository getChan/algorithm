from collections import deque
n, k = [int(_) for _ in input().split()]
left = [int(_) for _ in input()]
right = [int(_) for _ in input()]

queue = deque([(0, True)]) # (위치, 줄의 정보(True : left, False:right))
visited = {(0, True)}
level = 0
while queue:
    for _ in range(len(queue)):
        pos, line = queue.popleft()
        # print(pos, line)
        if pos+k >= n:
            queue = None
            print(1)
            break
        if pos < n-1\
            and (pos+1, line) not in visited:
            if line and left[pos+1]:
                visited.add((pos+1, line))
                queue.append((pos+1, line))
            elif not line and right[pos+1]:
                visited.add((pos+1, line))
                queue.append((pos+1, line))
        if (pos-1, line) not in visited \
            and pos-1 > level:
            if line and left[pos-1]:
                visited.add((pos-1, line))
                queue.append((pos-1, line))
            elif not line and right[pos-1]:
                visited.add((pos-1, line))
                queue.append((pos-1, line))
        if pos+k < n \
            and (pos+k, not line) not in visited:
            if line and right[pos+k]: 
                visited.add((pos+k, not line))
                queue.append((pos+k, not line))
            elif not line and left[pos+k]:
                visited.add((pos+k, not line))
                queue.append((pos+k, not line))
    level += 1
    # print(level)
if queue != None:
    print(0)