from sys import stdin
read = stdin.readline

h, w = map(int, read().rstrip().split())

for _ in range(h):
    cnt = -1
    for item in read().rstrip():
        if item == 'c':
            cnt = 0
        elif cnt != -1:
            cnt += 1
        print(cnt, end=' ')
    print()
