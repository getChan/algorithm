from sys import stdin
read = stdin.readline

case = int(read().rstrip())

def search(row, col, n):
    global maps
    global memo
    #기저 사례
    if row > n-1 or col > n-1:
        return False
    if row == n-1 and col == n-1:
        return True
    # 메모이제이션에 있다면
    if memo[row][col] != -1:
        return memo[row][col]
    memo[row][col] = search(row+maps[row][col], col, n) or search(row, col+maps[row][col], n)
    return memo[row][col]
    
for _ in range(case):
    n = int(read().rstrip())
    memo = [[-1 for __ in range(n)] for _ in range(n)]
    maps = [[int(x) for x in read().rstrip().split()] for _ in range(n)]
    if search(0, 0, n):
        print('YES')
    else:
        print('NO')