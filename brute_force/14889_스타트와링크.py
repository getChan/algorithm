from itertools import combinations
from sys import stdin
input = stdin.readline
n = int(input().rstrip())
s = list()
for _ in range(n):
    s.append([int(_) for _ in input().rstrip().split()])

def get_total_stat(team):
    '''
    팀의 총스탯 반환
    '''
    global s
    total = 0
    for i in team:
        for j in team:
            total += s[i][j]
    return total

answer = 400*10000
for case in combinations(range(n),n//2):
    team_a = case
    team_b = set(range(n))-set(case)
    stat_a = get_total_stat(team_a)
    stat_b = get_total_stat(tuple(team_b))
    if abs(stat_a-stat_b) < answer:
        answer = abs(stat_a-stat_b)
print(answer)
