from sys import stdin
import heapq
input = stdin.readline
n = int(input().rstrip())
heap = []
for _ in range(n):
    num = int(input().rstrip())
    if num > 0:
        heapq.heappush(heap, -num)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print('0')
