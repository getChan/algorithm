from sys import stdin
from collections import deque
input = stdin.readline

n, m, k = [int(x) for x in input().rstrip().split()]
arr = [[5 for _ in range(n)] for __ in range(n)]
A = []
for _ in range(n):
    A.append([int(x) for x in input().rstrip().split()])

trees = [[[] for _ in range(n)] for __ in range(n)]
for _ in range(m):
    x, y, age = [int(x) for x in input().rstrip().split()]
    trees[x-1][y-1].append(age)  # 나이가 어린 나무부터 양분을 먹는다.
    trees[x-1][y-1] = deque(sorted(trees[x-1][y-1]))


def year(trees):
    new_trees = [[deque() for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            dead = 0 # 죽은 나무들
            for _ in range(len(trees[i][j])):
                tree = trees[i][j].popleft()
                if arr[i][j] < tree:
                    # 땅에 양분이 부족하면 죽는다.
                    # 죽은 나무는 양분이 된다.
                    dead += tree//2
                else:
                    arr[i][j] -= tree
                    tree += 1
                    new_trees[i][j].append(tree)
            for p in new_trees[i][j]:  # 나이가 증가한 나무들
                if p % 5 == 0:  # 나무가 번식한다면
                    for di, dj in[(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        if not (0 <= i+di < n and 0 <= j+dj < n):
                            continue
                        else:
                            new_trees[i+di][j+dj].appendleft(1)
            # 봄에 죽은 나무들 양분 추가
            arr[i][j] += dead
            # 겨울에 양분 추가
            arr[i][j] += A[i][j]
    return new_trees


for _ in range(k):
    trees = year(trees)


answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)