from collections import defaultdict, deque
n, m, v = [int(_) for _ in input().split()]
graph = defaultdict(list)
for _ in range(m):
    fro, to = [int(_) for _ in input().split()]
    graph[fro].append(to)
    graph[to].append(fro)

visited = []
def dfs(v):
    global graph, visited
    visited.append(v)
    print(v, end=' ')
    for to in sorted(graph[v]):
        if to not in visited:
            dfs(to)
    return
dfs(v)
print()
visited = []
def bfs(v):
    global graph, visited
    visited.append(v)
    print(v, end=' ')
    queue = deque(sorted(graph[v]))
    while queue:
        to = queue.popleft()
        if to not in visited:
            print(to, end=' ')
            visited.append(to)    
            queue.extend(sorted(graph[to]))
bfs(v)