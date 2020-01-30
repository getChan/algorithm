from collections import deque
s = int(input())

def bfs(s):
    time = 0
    queue = deque([(1, 0)]) # (display, clipboard)
    visited = set()
    while queue:
        for _ in range(len(queue)):
            display, clipboard = queue.popleft()
            if display == s:
                return time
            
            # 클립보드에 저장하는 연산
            if (display, display) not in visited:
                visited.add((display, display))
                queue.append((display, display))
            # 화면에 붙여넣기 연산
            if (display+clipboard, clipboard) not in visited\
                and clipboard:
                visited.add((display+clipboard, clipboard))
                queue.append((display+clipboard, clipboard))
            # 이모티콘 하나 삭제 연산
            if (display-1, clipboard) not in visited\
                and display-1 >= 1:
                visited.add((display-1, clipboard))
                queue.append((display-1, clipboard))
        
        time += 1

print(bfs(s))