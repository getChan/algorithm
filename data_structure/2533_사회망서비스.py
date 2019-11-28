from sys import setrecursionlimit, stdin
setrecursionlimit(1000000)
input = stdin.readline
n = int(input().rstrip())
tree = [[] for _ in range(n+1)] # 2차원 인접 리스트
for _ in range(n-1):
    n1, n2 = [int(x) for x in input().rstrip().split()]
    tree[n1].append(n2)
    tree[n2].append(n1)

# DFS
# 1. 단말 노드이면 연결된 노드는 얼리어답터
# 2. 연결된 노드가 모두 얼리어답터 아니면 무조건 얼리어답터
early = set()
visited = set()
def dfs(n):
    global tree, early, visited
    visited.add(n)
    if len(tree[n]) <= 1:
        return True # 단말노드이다
    for i in tree[n]:
        if not i in visited:
            if dfs(i):
                early.add(n)
            elif not i in early: # 연결된 노드가 얼리어답터 아니면
                early.add(n)
    return False
for i, start in enumerate(tree):
    if len(start) > 1:
        dfs(i)
        break
if n==2:
    print(1)
else:
    print(len(early))