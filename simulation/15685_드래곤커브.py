from sys import stdin
input = stdin.readline
arr = [[0 for _ in range(101)] for __ in range(101)]
points = set()
def rotate(pivot_x, pivot_y, d, g):
    if d == 0:
        rot = lambda x, y : 
    elif d == 1:
    elif d == 2:
        rot = lambda x, y : pivot_x-pivot_x-x, 
    elif d == 3:
        
    
    
n = int(input().rstrip())
for _ in range(n):
    x, y, d, g = [int(x) for x in input().rstrip().split()]

    next_x, next_y = x, y
    arr[y][x] = 1
    points.add((x, y))
    if d == 0:
        next_x += 1
    elif d == 1:
        next_y -= 1
    elif d == 2:
        next_x -= 1
    elif d == 3:
        next_y += 1
        d = -1
    arr[next_y][next_x] = 1
    points.add((next_x, next_y))

    rotate(next_x, next_y, d+1, g)