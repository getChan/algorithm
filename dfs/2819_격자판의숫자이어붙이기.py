from sys import setrecursionlimit
setrecursionlimit(10000)
t = int(input())
def dfs(arr, x, y, num, result):
    num += arr[y][x]
    if len(num) >= 7:
        result.add(num)
        return
    if x-1 >= 0:
        dfs(arr, x-1, y, num, result)
    if x+1 < 4:
        dfs(arr, x+1, y, num, result)
    if y-1 >= 0:
        dfs(arr, x, y-1, num, result)
    if y+1 < 4:
        dfs(arr, x, y+1, num, result)

for tc in range(t):
    arr = []
    result = set()
    for _ in range(4):
        arr.append(input().split())
    for y in range(4):
        for x in range(4):
            dfs(arr, x, y, '', result)
    print('#{} {}'.format(tc+1, len(result)))