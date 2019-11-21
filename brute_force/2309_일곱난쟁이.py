from itertools import combinations
height = []
for _ in range(9):
    height.append(int(input()))

for case in combinations(height, 7):
    if sum(case) == 100:
        for _ in sorted(case):
            print(_)
        exit()