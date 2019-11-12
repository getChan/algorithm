def chknum(string):
    i = 1
    while i<=len(string)//2:
        if string[-2*i:-i] == string[-i:]:
            return False
        i+=1
    return True

def dfs(cur, n):
    if len(cur) == n:
        print(cur)
        exit()
    if chknum(cur+'1'):
        dfs(cur+'1', n)
    if chknum(cur+'2'):
        dfs(cur+'2', n)
    if chknum(cur+'3'):
        dfs(cur+'3', n)

n = int(input())
dfs('', n)

