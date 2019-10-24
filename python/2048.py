def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

if __name__ == "__main__":
    T = int(input())
    mat = [[x for x in input().split()] for col in range(4)]
    
    print(mat)