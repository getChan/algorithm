from sys import stdin
import heapq
from collections import deque
input = stdin.readline

heap = []
n = int(input().rstrip())
for _ in range(n):
    heapq.heappush(heap, int(input().rstrip()))
first = heapq.heappop(heap)
queue = deque([first], 5)
answer = (5-len(queue))
while heap:
    queue.append(heapq.heappop(heap))
    need = 0
    need += queue[-1]-queue[0]+1-len(queue)
    need += (5-len(queue))
    if need < answer:
        answer = need

print(answer)