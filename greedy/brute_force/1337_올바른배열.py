from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

if len(arr) < 5:
    arr.extend((5-len(arr))*[0])
prev = -1
i = 0
maximum = 0
while i < len(arr)-4:
    cnt = 1
    j = i
    while j < i+4:
        if arr[j+1] - arr[j] == 1:
            cnt += 1
        j += 1 
    if cnt > maximum:
        maximum = cnt
    i += 1

print(5-maximum)