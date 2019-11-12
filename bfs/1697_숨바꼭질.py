# DAG 그래프로 추상화하여 BFS로 풀어야 한다.
from collections import deque
n, k = [int(_) for _ in input().split()]


visited = set()
visited.add(k)
queue = deque([k])
result = []
level = 0
while queue:
    for _ in range(len(queue)):
        item = queue.popleft()
        if item == n:
            result.append(level)
        if item < n:
            if item == 0:
                result.append(abs(n-item)) 
            elif n-item < 2*item-n:
                result.append(level+abs(n-item))
            else:
                result.append(level-1+abs(2*item-n))
        if item%2 == 1:
            if item-1 not in visited:
                visited.add(item-1)
                queue.append(item-1)
            if item+1 not in visited:
                visited.add(item+1)
                queue.append(item+1)
        else :
            if item//2 not in visited:
                visited.add(item//2)
                queue.append(item//2)
    level += 1
print(min(result))