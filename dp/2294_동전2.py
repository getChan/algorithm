from sys import stdin
input = stdin.readline
n, k = [int(x) for x in input().rstrip().split()]
coins = set()
for _ in range(n):
    tmp = int(input().rstrip())
    if tmp <= k:
        coins.add(tmp)
# BFS로 풀수 있겠는데?
from collections import deque
coins = sorted(list(coins), reverse=True)
queue = deque(coins)
visited = set()
visited.update(coins)
cnt = 0
success = False
while queue and not success:
    cnt += 1
    # print(queue)
    for i in range(len(queue)):
        cost = queue.popleft()
        if cost == k:
            success = True
            queue = None
            break
        for c in coins:
            if cost+c <= k and cost+c not in visited:
                visited.add(cost+c)
                queue.append(cost+c)
    
if success:
    print(cnt)
else:
    print(-1)
