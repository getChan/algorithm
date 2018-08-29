from sys import stdin
read = stdin.readline
from operator import itemgetter

n, k = (int(x) for x in read().rstrip().split())

country = []

for _ in range(n):
    country.append([int(x) for x in read().rstrip().split()])

country.sort(key=itemgetter(1, 2, 3), reverse=True)

rank = 1
dump = 1
for index, c in enumerate(country):
    if c[0] == k:
        print(rank)
        break
    if c[1:] == country[index+1][1:]:
        dump += 1
        continue
    rank += dump
    dump = 1
