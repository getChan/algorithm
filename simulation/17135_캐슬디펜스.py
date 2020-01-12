from sys import stdin
from itertools import combinations
from copy import deepcopy

input = stdin.readline

n, m, d = [int(x) for x in input().rstrip().split()]
maps = []
for _ in range(n):
    maps.append([int(x) for x in input().rstrip().split()])

def kill_nearest_target(r, c, d, maps):
    '''
    BFS로 가장 가까운 타깃 찾는다
    '''
    queue = [(r-1, c)]
    level = 1
    while queue and level <= d:
        for _ in range(len(queue)):
            rr, cc = queue.pop(0)
            if maps[rr][cc]: # 적이 있으면
                return (rr, cc)
            if cc > 0:
                queue.append((rr, cc-1))
            if rr > 0:
                queue.append((rr-1, cc))
            if cc < m-1:
                queue.append((rr, cc+1))
        level += 1
    return False
    

def game(archeries, maps):
    total_kill = 0
    for archery_row in range(n, 0, -1):
        tmp_kill = set()
        for archery_col in archeries:
            target = kill_nearest_target(archery_row, archery_col, d, maps)
            if target:
                tmp_kill.add(target)
        total_kill += len(tmp_kill)
        for r, c in tmp_kill:
            maps[r][c] = 0
    return total_kill
        

print(max(game(archery, deepcopy(maps)) for archery in combinations(range(m), 3)))