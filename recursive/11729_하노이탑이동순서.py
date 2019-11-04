n = int(input())

move = []
cnt = 0
def hanoi(m, fro, by, to): # m개 원반을 fro에서 by를 거쳐 to로 보낸다.
    global cnt
    global move
    if m == 1:
        move.append([fro, to])
    else:
        hanoi(m-1, fro, to, by) # m-1 개 원반을 to를 거쳐 by로 옮긴다.
        move.append([fro ,to])# 1개 원반을 to로 옮긴다.
        hanoi(m-1, by, fro, to) # m-1개 by에 있는 원반을 fro 거쳐 to로 옮긴다.
    cnt += 1

hanoi(n, 1, 2, 3)
print(cnt)
for m in move:
    print(m[0], m[1])