from collections import deque
floor, start, goal, up, down = [int(x) for x in input().split()]

queue = deque([start])
visited = set()
step = 0
while queue:
    for _ in range(len(queue)):
        current = queue.popleft()
        if current == goal:
            print(step)
            queue = None
            break
        if current+up not in visited\
            and current+up <= floor:
            visited.add(current+up)
            queue.append(current+up)
        if current-down not in visited\
            and current-down >= 1:
            visited.add(current-down)
            queue.append(current-down)
    step += 1
if queue != None:
    print('use the stairs')