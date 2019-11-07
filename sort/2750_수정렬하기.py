import heapq
n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))
for _ in range(len(arr)):
    print(heapq.heappop(arr))
