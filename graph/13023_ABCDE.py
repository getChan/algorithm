from sys import stdin
from collections import deque
input = stdin.readline

# 모든 노드에 대해 사이클 없이 5번 탐색하는지 
# 모든 노드에서 DFS를 시작하면서 5단계까지 가면 성공

v, e = [int(x) for x in input().rstrip().split()]
adj = [list() for _ in range(v)]
for __ in range(e):
    v1, v2 = [int(x) for x in input().rstrip().split()]
    adj[v1].append(v2)
    adj[v2].append(v1)
answer = False
def dfs(v, level):
    global answer
    if level == 5:
        answer = True
        return
    for u in adj[v]:
        if u not in visited:
            visited.add(u)
            dfs(u, level+1)
        if answer == True:
            return
    visited.discard(v)

for i in range(v):
    visited = set([i])
    dfs(i, 1)
    if answer:
        print(1)
        break
else:
    print(0)