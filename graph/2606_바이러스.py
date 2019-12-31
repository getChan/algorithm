from sys import stdin
input = stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
networks = [list() for _ in range(n+1)]
for _ in range(m):
    fro, to = [int(x) for x in input().rstrip().split()]
    networks[fro].append(to)
    networks[to].append(fro)
visited = {1}
queue = [1]
while queue:
    for _ in range(len(queue)):
        node = queue.pop(0) 
        for next_node in networks[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

print(len(visited)-1)

