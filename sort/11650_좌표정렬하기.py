from sys import stdin
input = stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append([int(x) for x in input().rstrip().split()])

arr.sort(key=lambda x:(x[0], x[1]))

for x, y in arr:
    print(x, y)