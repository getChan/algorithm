from sys import stdin
import heapq
input = stdin.readline

vertex, edge = [int(x) for x in input().rstrip().split()]
k = int(input().rstrip())
adj = [dict() for _ in range(vertex+1)]
for _ in range(edge):
    u, v, w = [int(x) for x in input().rstrip().split()]
    # 정점 간 여러 간선 있을 수 있음
    if v in adj[u]:
        adj[u][v] = min(adj[u][v], w)
    else:
        adj[u][v] = w

INF = 10*300000+1
# 다익스트라 최단경로 알고리즘
def dijkstra(adj, k):
    dist = [INF for _ in range(len(adj))]
    dist[k] = 0

    # 우선순위 큐를 이용해 가장 짧은 경로를 가진 노드부터 방문한다.
    pq = []
    heapq.heappush(pq, (dist[k], k))
    while pq:
        _, u = heapq.heappop(pq)
        if dist[u] < _: 
            # 최적화
            # 큐에 넣었던 경로보다 더 짧은 경로로 업데이트되었을 경우
            continue
        # 인접한 노드에 대해서
        for v, w in adj[u].items():
            # 더 짧은 경로가 발견되었을 때
            if dist[v] > dist[u]+w:
                # 최단 경로 업데이트하고
                dist[v] = dist[u]+w
                # 이후 방문할 노드로 지정
                heapq.heappush(pq, (dist[v], v))
    
    return dist[1:]

for i in dijkstra(adj, k):
    if i < INF:
        print(i)
    else:
        print('INF')
