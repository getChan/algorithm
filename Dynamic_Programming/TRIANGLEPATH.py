from sys import stdin
read = stdin.readline

def triPath(row=0, col=0):
    # 기저 사례 : 마지막 줄
    global n
    global triangle
    if row == n-1:
        return triangle[row][col]
    # 메모이제이션
    if memo[row][col] != -1:
        return memo[row][col]
    memo[row][col] = triangle[row][col] + max(triPath(row+1, col), triPath(row+1, col+1))
    return memo[row][col]

c = int(read().rstrip())
for _ in range(c):
    memo = [[-1 for __ in range(101)] for x in range(101)]
    n = int(read().rstrip())
    triangle = []
    for __ in range(n):
        triangle.append([int(x) for x in read().rstrip().split()])
    print(triPath())