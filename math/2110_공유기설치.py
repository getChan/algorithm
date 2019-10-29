from functools import reduce
n, c = [int(_) for _ in input().split()]
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

x = 1
while True:
    cnt = 0
    if cnt == c:
        x += 1
        continue
    # 1 2 4 8 9
    #   1 2 4 1 