from sys import stdin
read = stdin.readline
n = int(read().rstrip())
line = []
for _ in range(n):
    line.append(int(read().rstrip()))
maxlen = 0
for i in line:
    length = 0
    cur = i
    for j in line[i+1:]:
        if cur<j:
            cur = j
            length += 1
    if maxlen < length:
        maxlen = length    

print(len(line)-maxlen)