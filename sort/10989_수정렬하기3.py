# import heapq
# from sys import stdin
# input = stdin.readline
# n = int(input().rstrip())
# arr = []
# for _ in range(n):
#     heapq.heappush(arr, int(input().rstrip()))
# for _ in range(n):
#     print(heapq.heappop(arr))

# 힙 정렬을 이용한 코드로는 메모리 초과 난다.
# 수의 범위가 10000 이하이므로 카운트 정렬 사용해보자

from sys import stdin
input = stdin.readline
n = int(input().rstrip())
counts = [0 for _ in range(10001)]
for _ in range(n):
    counts[int(input().rstrip())] += 1
idx = 1
for i in counts[1:]:
    for j in range(i):
        print(idx)
    idx += 1
