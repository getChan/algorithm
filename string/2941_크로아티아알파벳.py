from sys import stdin
input = stdin.readline
origin = input().rstrip()
cnt = 0
i = 0
while i < len(origin):
    try:
        if origin[i]=='c':
            if origin[i+1] in ['=', '-']:
                cnt += 1
                i += 2
                continue
        elif origin[i] == 'd':
            if origin[i+1] == 'z':
                if origin[i+2] == '=':
                    cnt += 1
                    i += 3
                    continue
            elif origin[i+1] == '-':
                cnt += 1
                i += 2
                continue
        elif origin[i] == 'l' and origin[i+1] == 'j':
            cnt += 1
            i += 2
            continue
        elif origin[i] == 'n' and origin[i+1] == 'j':
            cnt += 1
            i += 2
            continue
        elif origin[i] == 's' and origin[i+1] == '=':
            cnt += 1
            i += 2
            continue
        elif origin[i] == 'z' and origin[i+1] == '=':
            cnt += 1
            i += 2
            continue
    except IndexError:
        pass
    cnt += 1
    i += 1
print(cnt)