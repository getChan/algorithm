from collections import deque
n, k = [int(x) for x in input().split()]

queue = deque([int(x) for x in range(1,n+1)])
answer = '<'
while queue:
    for it in range(k):
        queue.rotate(-1)
    else:
        answer += str(queue.pop())+', '
    print
else:
    answer = answer[:-2]+'>'
print(answer)