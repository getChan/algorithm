arr = []
for idx in range(3):
    for jdx, item in enumerate([int(x) for x in input().split()]):
        if not item:
            i, j = idx, jdx

level = 0
queue = [(i, j)]
aligned = [[1,2,3],[4,5,6],[7,8,0]]
while queue:
    for _ in range(len(queue)):
        i, j = queue.pop(0)
        if (i, j) == (2, 2) and arr == aligned:
            break
            
    level += 1

