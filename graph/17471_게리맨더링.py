n = int(input())
popul = [int(x) for x in input().split()]
popul.insert(0, 0)

# 양방향 그래프다.
adj = [dict() for _ in range(n+1)]
for u in range(1, n+1):
    for v in input().split()[1:]:
        adj[u][v] = popul[v]
        adj[v][u] = popul[u]
