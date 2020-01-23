n, k = [int(x) for x in input().split()]

cnt = 0
flag = False
def dfs(num, string):
    global cnt, flag
    if num > n:
        return
    if num == n:
        cnt += 1
        if cnt == k:
            print(string[1:])
            flag = True
            return
    dfs(num+1, string+'+1')
    dfs(num+2, string+'+2')
    dfs(num+3, string+'+3')

dfs(0, '')
if not flag:
    print(-1)