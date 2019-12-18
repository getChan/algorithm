n = int(input())
max, min = -1000000, 1000000
for i in [int(x) for x in input().split()]:
    if i > max:
        max = i
    if i < min:
        min = i
print(min, max)