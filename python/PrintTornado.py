from sys import stdin
read = stdin.readline
# 소용돌이 map 생성
map =[[x for x in range(99)] for __ in range(99)]

row, col, num = 49, 49, 1
map[row][col] = num
inc = 0
while row<99 and row>=0 and col<99 and col>=0:
    try:
        inc += 1
        for i in range(inc):
            num += 1
            col += 1
            map[row][col] = num
        for i in range(inc):
            num += 1
            row -= 1
            map[row][col] = num
        inc += 1
        for i in range(inc):
            num += 1
            col -= 1
            map[row][col] = num
        for i in range(inc):
            num += 1
            row += 1
            map[row][col] = num
    except IndexError:
        break

r1, c1, r2, c2 = (int(x)+49 for x in read().rstrip().split())

for i in map[r1:r2+1]:
    for j in i[c1:c2+1]:
        
        print(j, end=' ')
    print()

