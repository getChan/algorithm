from sys import stdin
read = stdin.readline
n = int(read().rstrip())
seat = read().rstrip()

cnt = 2
Lisin = False
for i in seat:
    if i == 'L':
        cnt += 1
        Lisin = True
    else:
        cnt += 2

if not Lisin:
    cnt -= 2
print(cnt//2)
