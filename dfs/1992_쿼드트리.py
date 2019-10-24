def dfs(y, x, length):   
    global img
    chk = img[y][x]
    flag = True
    for i in range(y, y+length):
        if flag:
            for j in range(x, x+length):
                if img[i][j] != chk:
                    flag = False
                    break
        else:
            break
    if flag:
        return chk
    next_len = length//2
    res = '('
    res += dfs(y, x, next_len)
    res += dfs(y, x+next_len, next_len)
    res += dfs(y+next_len, x, next_len)
    res += dfs(y+next_len, x+next_len, next_len)
    return res + ')'

n = int(input())
img = []
for _ in range(n):
    img.append(list(input()))

print(dfs(0,0, len(img)))
