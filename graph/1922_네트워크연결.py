n = int(input())
m = int(input())
costs = []
for _ in range(m):
    costs.append([int(x) for x in input().split()])

def union_find(n1, n2, sets):
    if n1 > n2:
        n1, n2 = n2, n1
    if sets[n1] == sets[n2]:
        # cycle인 경우
        return False
    else:
        for i, v in enumerate(sets):
            if v == sets[n2] and i != n2:
                sets[i] = sets[n1]
        sets[n2] = sets[n1]
        
        return True

def Kruskal(costs):
    '''
    Kruskal Algorithm
    간선 선택을 기반으로 한 알고리즘
    Cycle이 생기지 않도록 해야 한다
    O(eloge * N) : 배열을 사용했기 때문에 N 곱해짐
    '''
    answer = 0
    sets = [_+1 for _ in range(n+1)]
    costs.sort(key=lambda x:x[2])
    for cost in costs:
        n1, n2, c = cost
        if union_find(n1, n2, sets):
            answer += c
        
    return answer

def Prim(costs):
    '''
    Prim Algorithm
    노드 선택을 기반으로 한 알고리즘
    O(N^2)
    <시간초과> : 알고리즘 수정이 필요
    '''
    nodes = [dict() for _ in range(n+1)]
    for cost in costs:
        n1, n2, c = cost
        nodes[n1][n2] = c
        nodes[n2][n1] = c
    selected = [False for _ in range(n+1)]
    selected[1] = True
    sets = set([1])

    answer = 0
    while sum(selected) < n:
        mini = [None, 10000]
        for s in sets:
            for k,v in nodes[s].items():
                if not selected[k] and v < mini[1]:
                    mini = [k, v]
        sets.add(mini[0])
        selected[mini[0]] = True
        answer += mini[1]
    return answer

print(Prim(costs))


