from sys import stdin
read = stdin.readline

def jlis(ai, bi):
    #기저 사례가 없다.
    if memo[ai][bi] != -1:
        return memo[ai][bi]
    # a[ai], b[bi]가 이미 존재하기 떄문에 길이는 최하 2
    ret = 2
    if ai == 0:
        ma = -1
    else:
        ma = a[ai]
    if bi == 0:
        mb = -1
    else:
        mb = b[bi]
    maxElement = max(ma, mb)
    for j in range(ai, n-1):
        ai += 1
        if maxElement < a[j]:
            ret = max(ret, jlis(j, bi)+1)
    for j in range(bi, m-1):
        bi += 1
        if maxElement < b[j]:
            ret = max(ret, jlis(ai, j)+1)
    memo[ai][bi] = ret
    return ret

c = int(read().rstrip())

for _ in range(c):
    n, m = [int(x) for x in read().rstrip().split()]

    a = [int(x) for x in read().rstrip().split()]
    b = [int(x) for x in read().rstrip().split()]

    memo = [[-1 for __ in range(m+1)] for ___ in range(n+1)]
    
    maxlen = 0

    for i in range(n):
        maxlen = max(maxlen, jlis(i, 0))
    for j in range(m):
        maxlen = max(maxlen, jlis(0, j))

    print(memo)        
    print(maxlen)

