from collections import defaultdict, deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)
input = stdin.readline
def search(fro, to, tree, dist, visited):
    # print(visited)
    for k, v in tree[fro].items():
        # print(fro, k, to)
        if k == to:
            return dist + tree[fro][to]
        else:
            if k not in visited:
                visited.add(k)
                rst = search(k, to, tree, dist+v, visited)
                if rst:
                    return rst
            



n = int(input().rstrip())
tree = [defaultdict(int) for _ in range(n+1)]
for _ in range(n-1):
    f, t, dist = [int(x) for x in input().rstrip().split()]
    tree[f][t] = dist
    tree[t][f] = dist
m = int(input().rstrip())
for _ in range(m):
    a, b = [int(x) for x in input().rstrip().split()]
    print(search(a, b, tree, dist=0, visited=set([a])))