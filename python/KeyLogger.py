# 이 문제는 stack개념을 사용하여 해결하면 더 빠르다.
from sys import stdin
read = stdin.readline
from collections import deque

n = int(read())

for _ in range(n):
    pw = read().rstrip()
    output = deque()
    cursor = 0
    for i in pw:
        if i == '<':
            if cursor > 0:
                cursor -= 1
        elif i == '>': 
            if cursor < len(output):
                cursor += 1
        elif i == '-':
            if cursor > 0:
                del output[cursor-1]
                cursor -= 1
        else:
            output.insert(cursor, i)
            cursor += 1
    print(''.join(output))

