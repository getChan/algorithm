# 정렬을 유지하며 삽입하는 방법.
# 1. 순차 탐색
n = int(input())
nums = []
for step in range(n):
    num = int(input())
    insert_idx = 0
    for idx, i in enumerate(nums):
        if i > num:
            insert_idx = idx
            break
    else:
        insert_idx = len(nums)
    nums.insert(insert_idx, num)
    
    print(nums[(len(nums)-1)//2])

# 당연히 위처럼 하면 시간초과 난다 (N^2)
# 2. 이분 탐색으로도 시도해 보자 (nlogn)
from sys import stdin
input = stdin.readline
def binary_search(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid+1
    return right

n = int(input().rstrip)
nums = []
for step in range(n):
    num = int(input().rstrip)
    insert_idx = 0
    
    insert_idx = binary_search(nums, num)
    
    nums.insert(insert_idx, num)
    # print(nums)
    print(nums[(len(nums)-1)//2])

# 위 방법으로 nlogn 만에 성공한다.
# 그러나 힙을 이용하면 더 빠르게 해결할 수 있을 것 같다.

from sys import stdin
import heapq
input = stdin.readline
def heap_solution(min_heap, max_heap, target):
    # max_heap의 루트 노드가 중간값
    # max_heap의 루트는 항상 min_heap의 루트보다 같거나 작아야 한다
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -target)
    else:
        heapq.heappush(min_heap, target)
    if min_heap and -max_heap[0] > min_heap[0]:
        max_insert = -heapq.heappop(min_heap)
        min_insert = -heapq.heappop(max_heap)
        
        heapq.heappush(max_heap, max_insert)
        heapq.heappush(min_heap, min_insert)

n = int(input().rstrip())
min_heap, max_heap = [], []
for step in range(n):
    num = int(input().rstrip())
    
    heap_solution(min_heap, max_heap, num)
    print(-max_heap[0])