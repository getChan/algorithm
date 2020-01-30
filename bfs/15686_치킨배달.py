from sys import stdin
# from collections import deque
from itertools import combinations
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
city = []
for _ in range(n):
    city.append([int(__) for __ in input().rstrip().split()])

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))

MAX_DIST = 2*n
answer = []
for case in combinations(chicken, m):
    city_dist = 0
    for hi, hj in house:
        dist = MAX_DIST
        for ci, cj in case:
            if dist > abs(ci-hi)+abs(cj-hj):
                dist = abs(ci-hi)+abs(cj-hj)
        city_dist += dist
    answer.append(city_dist)
        
print(min(answer))