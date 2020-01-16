from sys import stdin
from collections import deque
input = stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
adj = [set() for _ in range(n)]
for u in range(n):
    for v, flag in enumerate(input().rstrip().split()):
        if int(flag):
            adj[u].add(v)
            adj[v].add(u)
plan = {int(x)-1 for x in input().rstrip().split()}
city = plan.pop()
visited = set()
queue = deque([city])
visited.add(city)
while queue:
    city = queue.popleft()
    plan.discard(city)
    for adj_city in adj[city]:
        if adj_city not in visited:
            visited.add(adj_city)
            queue.append(adj_city)
if plan:
    print('NO')
else:
    print('YES')
