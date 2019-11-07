import heapq
from sys import stdin
input = stdin.readline
n = int(input().rstrip())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input().rstrip()))
for _ in range(n):
    print(heapq.heappop(arr))
