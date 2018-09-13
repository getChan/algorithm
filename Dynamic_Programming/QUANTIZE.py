# 각 숫자별 오차 제곱의 합을 최소화하는 양자화
def Quantization(s):
    squareSum = sum(map(lambda x : (x-s)*(x-s), num))
    return squareSum

from sys import stdin
read = stdin.readline
import math
c = int(read().rstrip())
for _ in range(c):
    n, s = (int(x) for x in read().rstrip().split())
    num = [int(x) for x in read().rstrip().split()]
    memo = [-1 for _ in range(1000)]

    rst = math.inf
    for i in range(min(num), max(num)+1):
        v = Quantization(i)
        if v < rst:
            rst = v
    print(rst)

