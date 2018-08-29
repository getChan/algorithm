from sys import stdin
read = stdin.readline

case = int(read().rstrip())
for i in range(case):
    w = read().rstrip()
    n = int(read().rstrip())
    files = []
    for j in range(n):
        files.append(read().rstrip())
    for f in files:
        