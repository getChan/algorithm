from sys import stdin
from collections import defaultdict
input = stdin.readline
n = int(input().rstrip())
alphabet_cnt = defaultdict(int)
for _ in range(n):
    word = input().rstrip()
    for i, ch in enumerate(word):
        alphabet_cnt[ch] += 10**(len(word)-i-1)
answer = 0
num = 9
for cnt in sorted(alphabet_cnt.values(), reverse=True):
    answer += num*cnt
    num -= 1

print(answer)