from sys import stdin
import heapq
input = stdin.readline
INF = 1000*800+1

n, e = [int(x) for x in input().rstrip().split()]
adj = [dict() for _ in range(n+1)]
for _ in range(e):
    u, v, w = [int(x) for x in input().rstrip().split()]
    if v in adj[u] and adj[u][v] < w:
        pass
    else:
        adj[u][v] = w
    if u in adj[v] and adj[v][u] < w:
        pass
    else:
        adj[v][u] = w
    
v1, v2 = [int(x) for x in input().rstrip().split()]

def dijkstra(adj, start, goal):    
    dist = [INF for _ in range(len(adj))]
    pq = []
    dist[start] = 0
    heapq.heappush(pq, (dist[start], start))

    while pq:
        prev_dist, u = heapq.heappop(pq)
        # 모든 노드에 대해 최단경로 볼 필요 없다
        # 목표 노드에 대해서만 구하면 됨
        # 거리가 작은 순으로 탐색함에 주의
        if u == goal:
            return dist[goal]
        if dist[u] < prev_dist:
            continue
        for v, w in adj[u].items():
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
                heapq.heappush(pq, (dist[v], v))
    return dist[goal]

one = dijkstra(adj, 1, v1) + dijkstra(adj, v2, n)
two = dijkstra(adj, 1, v2) + dijkstra(adj, v1, n)
between = dijkstra(adj, v1, v2)
if one >= INF and two >= INF or between == INF:
    print(-1)
elif one <= two:
    print(one+between)
else:
    print(two+between)
