from collections import deque
n, k = [int(x) for x in input().split()]
visited = [False for _ in range(2*max(n, k)+2)]
time = 0
queue = deque([n])
visited[n] = True
if k < n:
    print(n-k)
else:
    while queue:
        # print(queue)
        for _ in range(len(queue)):
            if not queue:
                break
            i = queue.popleft()
            while i <= 2*max(n, k):
                if i == k:
                    print(time)
                    queue = None
                    break
                visited[i] = True
                if i < 2*max(n, k)+1 and not visited[i+1]:
                    visited[i+1] = True
                    queue.append(i+1)
                if i > 0 and not visited[i-1]:
                    visited[i-1] = True
                    queue.append(i-1)
                if i == 0:
                    break
                i *= 2

        time += 1