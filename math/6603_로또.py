from sys import stdin
from itertools import combinations
input = stdin.readline

while True:
    k, *setnum = [int(x) for x in input().rstrip().split()]
    if k == 0:
        break
    for lotto in combinations(setnum, 6):
        print(' '.join(map(str, lotto)))
    print()