from sys import stdin
read = stdin.readline
n = int(read().rstrip())
arr = []
for i in range(n):
    arr.append(int(read().rstrip()))
arr.sort()

print(4-cnt)