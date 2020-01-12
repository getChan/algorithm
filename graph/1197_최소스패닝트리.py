from sys import stdin
import heapq
input = stdin.readline

n, e = [int(x) for x in input().rstrip().split()]

# Kruskal - 가중치가 낮은 간선부터 선택. 
# 간선에 연결된 노드 둘 다 선택되어 같은 집합이면 후보에서 제외
# 다른 집합이면 간선 선택

edges = []
disjoint_set = [_ for _ in range(n+1)] 
# disjoint_set[i] : i번 노드는 disjoint_set[i]번 노드의 집합에 속한다
for _ in range(e):
    u, v, w = [int(x) for x in input().rstrip().split()]
    heapq.heappush(edges, (w, u, v))
    
def find(u, disjoint_set):
    '''
    부모 노드를 찾는다.
    '''
    if u == disjoint_set[u]:
        return u
    # 부모 노드를 업데이트
    disjoint_set[u] = find(disjoint_set[u], disjoint_set)
    return disjoint_set[u]
def union(u, v, disjoint_set):
    '''
    u노드와 v노드가 같은 집합에 있으면 그대로
    다른 집합에 있으면 union
    '''
    u = find(u, disjoint_set)
    v = find(v, disjoint_set)
    if u == v: # 같은 집합에 있으면
        return False
    # 다른 집합에 있으면
    disjoint_set[v] = u
    return True

answer = 0
while edges:
    w, u, v = heapq.heappop(edges)
    if union(u, v, disjoint_set):
        answer += w    
print(answer)