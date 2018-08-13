from sys import stdin
read = stdin.readline
n, l = map(int, read().rstrip().split())
map = [[int(x) for x in read().rstrip().split()] for _ in range(n)]

cnt = 0
for row in map:
    i = 0
    for height in row[l:]:
        i += 1

        if map(lambda x: row[i]-x <= 1, row[i-l:i]) == True:
            continue
        else:
            break
        cnt += 1

print(cnt)