from sys import stdin
read = stdin.readline
from itertools import permutations

n = int(read().rstrip())
a = read().rstrip().replace(" ", "")
opernum = [int(x) for x in read().rstrip().split()]

oper = opernum[0]*'+'+opernum[1]*'-'+opernum[2]*'*'+opernum[3]*'//'

max = int(-10e8)
min = int(10e8)

for op in permutations(oper):
    txt = ''
    for i in range(len(op)):
        txt += (a[i]+op[i])
    txt += a[-1]
    print(txt)
    rst = eval(txt)
    if rst > max : max = rst 
    if rst < min : min = rst 

print(max)
print(min)
