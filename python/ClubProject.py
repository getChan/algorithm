from sys import stdin
read = stdin.readline

n = int(read().rstrip())
m = int(read().rstrip())
room = [1 for x in range(n+1)]
for _ in range(m):
    x, y = map(int, read().rstrip().split())
    room[x:y] = [0 for x in range(y-x)]
print(room.count(1)-1)
