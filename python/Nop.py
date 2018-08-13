from sys import stdin

oldprocessor = stdin.readline().rstrip()
index, sum, cnt = -3, -3, 0

for code in oldprocessor:
    if code.islower():
        cnt += 1
    else:
        if index%4 != 0:
            sum += 3-cnt%4
            index += 3-cnt%4
        cnt = 0
    index += 1

print(sum)