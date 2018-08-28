from sys import stdin

read = stdin.readline

n = int(read().rstrip())
num = list(map(int, read().rstrip().split()))
answer = num[-1]
num = num[:-1]

#메모이제이션 기법 적용하기
from collections import defaultdict
def memoize(func):
    tempMemo = defaultdict(dict)
    def wrapped(num, subtotal):
        if str(num) in tempMemo:
            if subtotal in tempMemo[str(num)]:
                return tempMemo[str(num)][subtotal]
        result = func(num, subtotal)
        tempMemo[str(num)][subtotal] = result
        return result
    return wrapped

@memoize
def add(num, subtotal):
    #기저 사례
    if subtotal < 0 or subtotal > 20:
        return 0
    if len(num) == 0:
        if subtotal == answer:
            return 1
        else:
            return 0
    subtotal += num[0]
    print(num, subtotal)
    return add(num[1:], subtotal) + sub(num[1:], subtotal)

@memoize
def sub(num, subtotal):
    #기저 사례
    if subtotal < 0 or subtotal > 20:
        return 0
    if len(num) == 0:
        if subtotal == answer:
            return 1
        else:
            return 0
    print(num, subtotal)
    subtotal -= num[0]
    return add(num[1:], subtotal) + sub(num[1:], subtotal)
        
subtotal = num[0]
print(add(num[1:], subtotal))