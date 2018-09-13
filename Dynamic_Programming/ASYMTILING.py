from sys import stdin
read = stdin.readline

# 메모이제이션 데코레이터 함수
# 제약 : 함수는 1개의 인자를 받아야 함, 인자는 딕셔너리의 키가 되어야 함.(hashable)
def memoize(func):
    tempMemo = dict()
    def wrapped(n):
        if n in tempMemo:
            return tempMemo[n]
        result = func(n)
        tempMemo[n] = result
        return result
    return wrapped

def asymetric(width):
    if width%2 == 1:
        return (tiling(width)-tiling(width/2)+MOD) % MOD
    ret = tiling(width)
    ret = (ret - tiling(width/2) + MOD) % MOD
    ret = (ret - tiling(width/2-1) + MOD) % MOD
    return ret

@memoize
def tiling(width):
    # 기저 사례 : 타일의 너비가 1이하로 남았을 때
    
    if width <= 1:
        return 1
    return (tiling(width-2) + tiling(width-1)) % 1000000007

c = int(read().rstrip())
for _ in range(c):
    n = int(read().rstrip())
    MOD = 1000000007
    print(asymetric(n))
    