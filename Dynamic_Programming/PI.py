from sys import stdin
read = stdin.readline

def classify(i, l):
    # 숫자 조각을 가져온다.
    num = pi[i:l]
    # 난이도 1 : 모든 숫자가 같다.
    if num == [num[0]]*len(num):
        return 1
    # 난이도 2 : 숫자가 1씩 단조 증가하거나 감소
    progressive = True
    for k in range(1, len(num)-1):
        if num[k+1] - num[k] != num[1]-num[0]:
            progressive = False
    if progressive and abs(num[1]-num[0]) == 1:
        return 2
    alternating = True
    for k in range(1, len(num)):
        if num[k] != num[k%2]:
            alternating = False
    if alternating:
        return 4
    if progressive:
        return 5
    else:
        return 10

def memorize(i):
    if i >= len(pi):
        return 0
    if memo[i] != -1:
        return memo[i]
    ret = 987654321 # 최대 크기
    for l in range(3, 6):
        ret = min(ret, memorize(i+l)+classify(i ,i+l-1))
    memo[i] = ret
    return memo[i]

c = int(read().rstrip())    

for _ in range(c):
    pi = [int(x) for x in read().rstrip()]
    memo = [-1 for __ in range(10002)]
    print(memorize(0))

