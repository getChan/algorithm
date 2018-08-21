# numbers = [int(x) for x in input().split()]

# 나의 쓰레기같은 알고리즘 ㅎㅎ
#-----------------------------
# numbers.sort()
# multiple = numbers[2]
# cnt = 0
# while cnt < 3:
#     cnt = 0
#     cnt = len(tuple(filter(lambda x: multiple%x == 0, numbers)))
#     multiple += 1 

# print(multiple-1)
# -------------------------------------------------------------------


# 완벽한 풀이
import itertools

# 유클리드 호제법 : gcd(a, b) = gcd(b, a%b)
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
# lcm(a, b) = a * b / gcd(a, b)    
def lcm(a, b):
    return a * b // gcd(a, b)
# 재귀, asterisk, 삼항연산자 개쩌는 조합
def lcms(*args):
    return lcm(*args) if len(args) == 2 else lcm(args[0], lcms(*args[1:]))

arr = [int(x) for x in input().split()]

almost_mult = (lcms(*xs) for xs in itertools.combinations(arr, r=3))
print(min(almost_mult))

