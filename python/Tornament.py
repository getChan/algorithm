n, a, b = (int(x) for x in input().split())

round = 0

while a != b:
    a = (a+1)//2
    b = (b+1)//2
    round += 1

print(round)