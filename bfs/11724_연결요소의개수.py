from sys import stdin
from collections import deque
input = stdin.readline

node, vertex = [int(_) for _ in input().rstrip().split()]
adj = [[] for _ in range(node)]
for _ in range(vertex):
    u, v = [int(_)-1 for _ in input().rstrip().split()]
    adj[u].append(v)
    adj[v].append(u)

visited = set()
answer = 0
for i in range(node):
    if i not in visited:
        answer += 1
        queue = deque([i])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
print(answer)