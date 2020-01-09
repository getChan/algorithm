from sys import stdin
import heapq
input = stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
adj = [dict() for _ in range(n+1)]
for _ in range(m):
    u, v, w = [int(x) for x in input().rstrip().split()]
    if v in adj[u] and adj[u][v] < w:
        pass
    else:
        adj[u][v] = w
start, target = [int(x) for x in input().rstrip().split()]

def dijkstra(adj, start):
    INF = 100000*1000+1
    dist = [INF for _ in range(len(adj))]
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (dist[start], start))

    while pq:
        prev_dist, u = heapq.heappop(pq)
        if prev_dist > dist[u]:
            continue
        for v, w in adj[u].items():
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

print(dijkstra(adj, start)[target])