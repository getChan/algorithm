from sys import stdin

input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
edges = []
for _ in range(m):
    edges.append([int(x) for x in input().rstrip().split()])
    

parents = [_ for _ in range(n+1)]
def find(u):
    if u != parents[u]:
        parents[u] = find(parents[u])
    return parents[u]

def union(u, v):
    up = find(u)
    vp = find(v)
    if up != vp:
        parents[vp] = up
        return True
    return False

answer = 0
disjoint_cnt = n
edges.sort(key=lambda x:x[2])
# disjoint set 의 수가 2개일때까지 union-find 진행하면 됨
for u, v, w in edges:
    if disjoint_cnt <= 2:
        break
    if union(u, v):
        disjoint_cnt -= 1
        answer += w

print(answer)