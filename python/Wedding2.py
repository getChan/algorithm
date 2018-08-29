from sys import stdin
read = stdin.readline

n = int(read().rstrip())
m = int(read().rstrip())

fset = set()
ffset = set()

pair = []
for _ in range(m):
    realation = [int(x) for x in read().split()]
    if realation[0] == 1:
        fset.add(realation[1])
    else:
        pair.append(tuple(realation))

for i in pair:
    if i[0] in fset or i[1] in fset:
        ffset.add(i[1])
        ffset.add(i[0])
print(len(fset|ffset))