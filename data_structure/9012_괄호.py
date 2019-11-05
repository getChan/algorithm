t = int(input())

for _ in range(t):
    stack = []
    st = input()
    for ch in st:
        if ch == '(':
            stack.append(ch)
        else:
            try:
                stack.pop()
            except:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')