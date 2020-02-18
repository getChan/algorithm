from sys import stdin
from collections import deque
input = stdin.readline


def bfs():
    while queue:
        i, j = queue.popleft()
        if (i, j) == goal:
            print("happy")
            return True

        for s in stores:
            if s not in visited and \
                    abs(s[0] - i) + abs(s[1] - j) <= 1000:
                visited.add(s)
                queue.append(s)

    return False


for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    i, j = [int(x) for x in input().rstrip().split()]
    stores = []
    for __ in range(n):
        stores.append(tuple(int(i) for i in input().rstrip().split()))
    goal = tuple(int(i) for i in input().rstrip().split())
    stores.append(goal)
    visited = {(i, j)}

    queue = deque()
    for s in stores:
        if abs(s[0]-i)+abs(s[1]-j) <= 1000:
            visited.add(s)
            queue.append(s)

    if not bfs():
        print("sad")