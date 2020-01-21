n = int(input())
s = [[None for _ in range(n)] for __ in range(n)]
string = [ch for ch in input()]
tmp = 0
for i in range(n):
    for j in range(i, n):
        s[i][j] = string[tmp]
        tmp += 1

avail_num = [{i for i in range(-10, 11)} for _ in range(n)]
def num_range(sign):
    if sign == '-':
        return {i for i in range(-10, 0)}
    elif sign == '+':
        return {i for i in range(1, 11)}
    else:
        return {0}

for i in range(n-1, -1, -1):
    for j in range(i, n):
        if i == j:
            avail_num[i] &= num_range(s[i][j])
        else:
            avail_num[i] avail_num[j]