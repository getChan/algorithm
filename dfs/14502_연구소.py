from sys import stdin
from copy import deepcopy
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
lab = []
for _ in range(n):
    lab.append([int(x) for x in input().rstrip().split()])

def dfs(i, j, lab):
    if j > 0 and not lab[i][j-1]:
        lab[i][j-1] = 2
        dfs(i, j-1, lab)
    if i > 0 and not lab[i-1][j]:
        lab[i-1][j] = 2
        dfs(i-1, j, lab)
    if j < m-1 and not lab[i][j+1]:
        lab[i][j+1] = 2
        dfs(i, j+1, lab)
    if i < n-1 and not lab[i+1][j]:
        lab[i+1][j] = 2
        dfs(i+1, j, lab)
    return lab

def infection(lab):
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                dfs(i, j, lab)

    safety = 0
    for i in lab:
        for j in i:
            if not j:
                safety += 1
    return safety

answer = 0
for a in range(m*n-2):
    if not lab[a//m][a%m]:
        lab[a//m][a%m] = 1
        for b in range(a+1, m*n-1):
            if not lab[b//m][b%m]:
                lab[b//m][b%m] = 1
                for c in range(b+1, m*n):
                    if not lab[c//m][c%m]:
                        lab[c//m][c%m] = 1
                        result = infection(deepcopy(lab))
                        if result > answer:
                            answer = result
                        lab[c//m][c%m] = 0
                lab[b//m][b%m] = 0
        lab[a//m][a%m] = 0

print(answer)