from sys import stdin

def SearchTri(row=0, col=0):
    # 기저 사례
    if row+1 == len(triangle):
        return triangle[row][col]
    # 저장되 있으면
    if memo[row][col] != -1:
        return memo[row][col]
    memo[row][col] = triangle[row][col] + max(SearchTri(row+1, col), SearchTri(row+1, col+1))
    return memo[row][col]

read = stdin.readline

n = int(read().rstrip())
triangle = [[int(x) for x in read().rstrip().split()] for _ in range(n)]
memo = [[-1 for _ in range(n)] for __ in range(n)]

print(SearchTri())
