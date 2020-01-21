from sys import stdin
input = stdin.readline

s = [False for _ in range(21)]
m = int(input().rstrip())
for _ in range(m):
    op = input().rstrip().split()
    if op[0] == 'add':
        s[int(op[1])] = True
    elif op[0] == 'remove':
        s[int(op[1])] = False
    elif op[0] == 'check':
        if s[int(op[1])]:
            print(1)
        else:
            print(0)
    elif op[0] == 'toggle':
        if s[int(op[1])]:
            s[int(op[1])] = False
        else:
            s[int(op[1])] = True
    elif op[0] == 'all':
        s = [True for _ in range(21)]
    else:
        s = [False for _ in range(21)]