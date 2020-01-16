from sys import stdin
from itertools import permutations
from collections import deque
input = stdin.readline

n = int(input().rstrip())
innings = []
for _ in range(n):
    innings.append([int(x) for x in input().rstrip().split()])

def attack(hitman, innings):
    score = 0
    queue = deque(hitman)
    for inning in innings:
        base = deque([False, False, False])
        out = 0
        while out < 3:
            tasuk = queue.popleft()
            if inning[tasuk] == 0:
                out += 1
            elif inning[tasuk] == 1:
                base.append(True)
                home = base.popleft()
                if home:
                    score += 1
            elif inning[tasuk] == 2:
                base.extend([True, False])
                for _ in range(2):
                    if base.popleft():
                        score += 1
            elif inning[tasuk] == 3:
                base.extend([True, False, False])
                for _ in range(3):
                    if base.popleft():
                        score += 1
            else:
                base.extend([False, False, False])
                for _ in range(3):
                    if base.popleft():
                        score += 1
                score += 1
            queue.append(tasuk)
    return score


answer = 0
# 타선의 모든 경우의 수
for hitman in permutations(range(1, 9)):
    hitman = list(hitman)
    hitman.insert(3, 0)
    score = attack(hitman, innings)
    if answer < score:
        answer = score
print(answer)