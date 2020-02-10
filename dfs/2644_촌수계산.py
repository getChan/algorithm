from sys import stdin
input = stdin.readline

n = int(input().rstrip())
adj = [list() for _ in range(n+1)]
d1, d2 = [int(_) for _ in input().rstrip().split()]
m = int(input().rstrip())
for _ in range(m):
    a1, a2 = [int(x) for x in input().rstrip().split()]
    adj[a1].append(a2)
    adj[a2].append(a1)

flag = True
def dfs(s, level):
    global flag
    if s == d2:
        print(level)
        flag = False
        return
    for i in adj[s]:
        if i not in visited:
            visited.add(i)
            dfs(i, level+1)

visited = {d1}
dfs(d1, 0)

if flag:
    print(-1)