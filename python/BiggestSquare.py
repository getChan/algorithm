from sys import stdin
read = stdin.readline

n, m = map(int, read().rstrip().split())

map = [[read().rstrip()] for _ in range(n)]

rowindex = 0
colindex = 0

for row in map:
    rowlen = 0
    for _ in row:
        if map[rowindex][colindex] == '1':
            rowlen += 1
            rowindex += 1
        else:
            for __ in range(colindex, m)
                try:
                    if map[rowindex-1][colindex] == '1'
                        collen += 1
                    else:

                except IndexError:
                    break
            collen = 0

        colindex += 1
    rowindex = 0


print(map)
