from sys import stdin
read = stdin.readline
n = int(read().rstrip())

matrix = []
for i in range(n):
    matrix.append([int(x) for x in read().split()])

print(matrix)

result = [[0 for __ in range(n)] for _ in range(n)]
for i, row in enumerate(matrix):
    for j, item in enumerate(row):
        if 