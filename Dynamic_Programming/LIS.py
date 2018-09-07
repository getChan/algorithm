from sys import stdin
read = stdin.readline

def lis(i):
    #기저 사례가 없다.
    if memo[i] != -1:
        return memo[i]
    #항상 seq[start]는 있기 때문에 길이는 최하 1
    ret = 1
    for j in range(i+1, n):
        if seq[i] < seq[j]:
            ret = max(ret, lis(j)+1)
    memo[i] = ret
    return ret

c = int(read().rstrip())

for _ in range(c):
    n = int(read().rstrip())
    seq = [int(x) for x in read().rstrip().split()]
    memo = [-1 for __ in range(n+1)]
    maxlen = 0
    for i in range(n):
        maxlen = max(maxlen, lis(i))
    print(maxlen)
