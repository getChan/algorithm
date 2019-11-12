from copy import deepcopy
n = int(input())
def dfs(i, j, chess):
    global n
    cnt = 0
    if i+1 >= n:
        return 1
    for c in range(n):
        if chess[i][c]:
            new_chess = deepcopy(chess)
            row = 1
            r, l = c+1, c-1
            while i+row<n:
                new_chess[i+row][c] = False
                if l >=0:
                    new_chess[i+row][l] = False
                if r < n:
                    new_chess[i+row][r] = False
                row += 1 
                r += 1
                l -= 1
            cnt += dfs(i+1, c, new_chess)
        else:
            return 0
        
    if i == 0:
        print(cnt)
# 백트래킹은 가능한 경우만 stack에 push한다
# 한 행에 2개 이상의 퀸은 올 수 없다.
chess = [[True for _ in range(n)] for __ in range(n)]
dfs(0, 0, chess)    
