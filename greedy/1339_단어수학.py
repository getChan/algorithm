from collections import defaultdict
n = int(input())
# 자릿수의 빈도를 구하자
alphabet = defaultdict([0 for _ in range(10)])
for _ in range(n):
    word = input()
    for ch in word[::-1]:
        


