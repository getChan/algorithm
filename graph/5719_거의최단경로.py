# 최단경로 알고리즘 적용 문제
# 두 번째 짧은 경로를 찾아야 한다.
# 노드 수는 500개 이하
# 단방향 그래프
# 다익스트라를 이용해보자
# 다익스트라는 시작 노드에서 모든 노드까지 최단거리 구한다.


from sys import stdin
import heapq
input = stdin.readline
MAXNUM = 10**7

def dijkstra(adj, start):
    dist = [MAXNUM for _ in range(len(adj))]
    dist[start] = 0

    pq = [(dist[start], start)]
    while pq:
        prev, u = heapq.heappop(pq)
        if prev > dist[u]:
            continue
        for v, w in adj[u].items():
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                heapq.heappush(pq, (dist[v], v))
    return dist


while True:
    node, weight = [int(x) for x in input().rstrip().split()]
    if not node+weight:
        break
    start, dest = [int(x) for x in input().rstrip().split()]
    adj = [dict() for _ in range(node)]
    for _ in range(weight):
        u, v, p = [int(x) for x in input().rstrip().split()]
        adj[u][v] = p
    dist = dijkstra(adj, start)
    # minimum = dist[dest]
    # answer = MAXNUM
    #
    # print(answer)



