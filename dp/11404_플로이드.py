from collections import defaultdict
n = int(input())
m = int(input())
MAXNUM = 100001
path = [defaultdict(MAXNUM) for _ in range(n+1)]
for _ in range(m):
    s, e, c = [int(x) for x in input().split()]
    if path[s][e]:
        if c < path[s][e]:
            path[s][e] = c
    else:
        path[s][e] = c
    
    dist = []
    for i in range(n):
        