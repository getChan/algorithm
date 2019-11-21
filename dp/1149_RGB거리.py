import sys
sys.setrecursionlimit(1000**3)
n = int(input())
costs = []
prev = -1
for _ in range(n):
    costs.append([int(__) for __ in input().split()])

def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
    
@memo
def search(rgb, n):
    global costs
    
    mini = 10000000
    for i in range(3):
        if i != rgb :
            if n == len(costs)-1:
                tmp = costs[n][i]
            else:
                tmp = costs[n][i]+search(i, n+1)
            if tmp < mini:
                mini = tmp
    return mini

if n == 2:
    print(min(costs[0])+min(costs[1]))
else:
    print(min(costs[0][0]+search(0, 1), costs[0][1]+search(1, 1), costs[0][2]+search(2, 1)))