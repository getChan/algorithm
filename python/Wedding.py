from sys import stdin
read = stdin.readline

read()
m = int(read())
friends = set()
ffriends = set()

pair = list()
for _ in range(m):  # 상근이의 친구들 리스트에 저장
    realation = read().split()
    if realation[0] == '1':
        friends.add(realation[1])
    else:
        pair.append(tuple(realation))

for i in pair:
    if i[0] in friends or i[1] in friends:
        ffriends.add(i[1])
        ffriends.add(i[0])

print(len(friends | ffriends))
