from sys import stdin
input = stdin.readline
n = int(input().rstrip())
stack = []
for _ in range(n):
    op = input().rstrip().split()
    if op[0] == 'push':
        stack.append(op[1])
    elif op[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    else:
        if stack:
            print(stack[-1])
        else:
            print('-1')
