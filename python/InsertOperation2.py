from sys import stdin
read = stdin.readline
from itertools import permutations
from functools import reduce
import time


def insert_operation(length, input_num, input_oper):
    ops = {"0": (lambda x,y : x+y), "1" : (lambda x,y : x-y), "2" : (lambda x,y : x*y), "3" : (lambda x,y : x//y)}
    oper_permutation = []
    result = []
    list(oper_permutation.extend(
    [str(index)]*value) for index, value in enumerate(input_oper) if value>0)
    permutation = [list(x) for x in set(permutations(oper_permutation))]
    for i in permutation:
        result.append(reduce(lambda x,y : ops[i.pop()](x,y), input_num))

    print(str(max(result))+'\n'+str(min(result)))

n = int(read().rstrip())
a = [int(x) for x in read().rstrip().split()]

oper = [int(x) for x in read().rstrip().split()]
insert_operation(n, a, oper)