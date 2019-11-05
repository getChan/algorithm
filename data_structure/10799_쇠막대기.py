s = input()
stack = 0
cnt = 0
prev = ''
for ch in s:
    if prev == '(' and ch == ')':
        stack -= 1
        cnt += stack
    else:
        if ch == '(':
            stack += 1
        else:
            stack -= 1
            cnt += 1
    prev = ch
print(cnt)

