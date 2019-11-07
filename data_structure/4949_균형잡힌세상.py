while True:
    s = input()
    if s == '.':
        break
    stack = []
    for ch in s:
        if ch == '(' or ch =='[':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif ch ==']':
            if not stack or stack.pop() != '[':
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')