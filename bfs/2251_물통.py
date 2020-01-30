from collections import deque
vacancy = [int(x) for x in input().split()]
water = vacancy.copy()
water[:2] = [0, 0]

queue = deque([2])
while queue:
    pos = queue.popleft()
    2-pos

