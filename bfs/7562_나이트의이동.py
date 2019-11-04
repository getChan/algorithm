from collections import deque
def bfs(ci, cj, queue):
    global visited
    l = len(visited)
    
    if ci-2 >= 0 and cj+1 < l and not visited[ci-2][cj+1]:
        visited[ci-2][cj+1] = 1
        queue.append((ci-2,cj+1))

    if ci-1 >= 0 and cj+2 < l and not visited[ci-1][cj+2]:
        visited[ci-1][cj+2] = 1
        queue.append((ci-1,cj+2))

    if ci-2 >= 0 and cj-1 >= 0 and not visited[ci-2][cj-1]:
        visited[ci-2][cj-1] = 1
        queue.append((ci-2,cj-1))

    if ci-1 >= 0 and cj-2 >= 0 and not visited[ci-1][cj-2]:
        visited[ci-1][cj-2] = 1
        queue.append((ci-1,cj-2))

    if ci+1 < l and cj+2 < l and not visited[ci+1][cj+2]:
        visited[ci+1][cj+2] = 1
        queue.append((ci+1,cj+2))

    if ci+2 < l and cj+1 < l and not visited[ci+2][cj+1]:
        visited[ci+2][cj+1] = 1
        queue.append((ci+2,cj+1))

    if ci+1 < l and cj-2 >= 0 and not visited[ci+1][cj-2]:
        visited[ci+1][cj-2] = 1
        queue.append((ci+1,cj-2))

    if ci+2 < l and cj-1 >= 0 and not visited[ci+2][cj-1]:
        visited[ci+2][cj-1] = 1
        queue.append((ci+2,cj-1))

    return queue
    

t = int(input())
for _ in range(t):
    l = int(input())
    cur = [int(__) for __ in input().split()]
    target = [int(__) for __ in input().split()]

    if cur == target:
        print(0)
        continue

    visited = [[0 for __ in range(l)] for __ in range(l)]
    
    queue = deque()

    level = 1
    visited[cur[0]][cur[1]] = 1 
    queue = bfs(*cur, queue)
    
    while queue:
        for q in range(len(queue)):
            i, j = queue.popleft()
            if [i, j] == target:
                print(level)
                break
            queue = bfs(i,j, queue)
        if [i, j] == target:
            break
        level += 1
        