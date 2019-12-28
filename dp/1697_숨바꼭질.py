from collections import deque
n, k = [int(x) for x in input().split()]
# BFS
queue = deque([n])
step = 0
visited = {n:step}
while queue:
    step += 1
    for _ in range(len(queue)):
        pos = queue.popleft()
        if pos == k:
            visited[k] = step-1
            queue = None
            break
        if pos <= k and pos+1 not in visited:
            visited[pos+1] = step
            queue.append(pos+1)
        if pos > 0 and pos-1 not in visited:
            visited[pos-1] = step
            queue.append(pos-1)
        if pos <= k and 2*pos not in visited:
            visited[2*pos] = step
            queue.append(2*pos)
print(visited[k])
