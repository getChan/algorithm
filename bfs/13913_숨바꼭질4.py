from collections import deque
n, k = [int(_) for _ in input().split()]
MAX_NUM = 100000
parent = [False for _ in range(MAX_NUM+1)] # 부모 노드를 가리키는 배열
visited = set()
queue = deque([n])
parent[n] = n
step = 0
while queue:
    for _ in range(len(queue)):
        current = queue.popleft()
        if current == k:
            print(step)
            queue = None
            break
        if current > 0 and current-1 not in visited:
            visited.add(current-1)
            parent[current-1] = current
            queue.append(current-1)
        if current < MAX_NUM and current+1 not in visited:
            visited.add(current+1)
            parent[current+1] = current
            queue.append(current+1)
        if 2*current <= MAX_NUM and 2*current not in visited:
            visited.add(2*current)
            parent[2*current] = current
            queue.append(2*current)
    step += 1

answer = []
while k != n:
    answer.append(k)
    k = parent[k]
answer.append(n)

for i in answer[::-1]:
    print(i, end=' ')