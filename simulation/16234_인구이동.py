from sys import stdin
from collections import deque
input = stdin.readline

n, l, r = [int(_) for _ in input().rstrip().split()]
country = []
for _ in range(n):
    country.append([int(__) for __ in input().rstrip().split()])

def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited.add((i, j))
    union = {(i, j)}
    while queue:
        ci, cj = queue.popleft()
        for di, dj in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            if (0<= ci+di <n) and (0<= cj+dj <n)\
                and (ci+di, cj+dj) not in visited\
                and l<= abs(country[ci+di][cj+dj] - country[ci][cj]) <= r:
                visited.add((ci+di, cj+dj))
                queue.append((ci+di, cj+dj))
                union.add((ci+di, cj+dj))
    return union

def search_opened():
    '''
    BFS로 국경이 열려야 하는 연합의 "집합" 찾는다.
    - 연합(국경이 개방되는 국가들)은 여러개 있을 수 있다.
    '''
    unions = []
    visited = set()
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                unions.append(bfs(i, j, visited))

    return unions

def move(unions):
    '''
    인구 이동을 시작한다.
    '''
    for union in unions:
        # 새 인구는 (연합의 인구수) // (연합 국가 수)
        new_popul = 0
        for ci, cj in union:
            new_popul += country[ci][cj]
        new_popul = new_popul // len(union)

        for ci, cj in union:
            country[ci][cj] = new_popul

answer = 0
unions = search_opened()
# 인구 이동이 있다 == 연합이 하나라도 있다.
# == 연합의 집합의 수가 국가 수와 같지 않다.
while len(unions) < n*n:
    answer += 1
    move(unions)
    unions = search_opened()
print(answer)