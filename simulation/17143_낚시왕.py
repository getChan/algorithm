from sys import stdin
input = stdin.readline


class Shark(object):
    def __init__(self, s, d, z):
        self.s = s
        self.d = d
        self.z = z

    def __repr__(self):
        return str(self.s)


def move(r, c, s, d, z, ss):
    if d == 1: # 위
        for i in range(s):
            if r == 0: # 부딪히면
                move(r, c, s-i, 2, z, ss)
                return
            r -= 1
    elif d == 2: # 아래:
        for i in range(s):
            if r == R-1:
                move(r, c, s-i, 1, z, ss)
                return
            r += 1
    elif d == 3: # 오른쪽
        for i in range(s):
            if c == C-1:
                move(r, c, s-i, 4, z, ss)
                return
            c += 1
    elif d == 4: # 왼쪽
        for i in range(s):
            if c == 0:
                move(r, c, s-i, 3, z, ss)
                return
            c -= 1

    if new_arr[r][c]: # 이미 상어 있으면
        if new_arr[r][c].z < z:
            new_arr[r][c] = Shark(ss, d, z)
    else:
        new_arr[r][c] = Shark(ss, d, z)
    return


R, C, M = [int(x) for x in input().rstrip().split()]
arr = [[0 for _ in range(C)] for __ in range(R)]
for _ in range(M):
    r, c, *args = [int(x) for x in input().rstrip().split()]
    r -= 1
    c -= 1
    shark = Shark(*args)
    arr[r][c] = shark

answer = 0
j = 0
while j < C:
    # 낚자
    for i in range(R):
        if arr[i][j]:
            answer += arr[i][j].z
            arr[i][j] = 0
            break
    # 움직이자
    new_arr = [[0 for _ in range(C)] for __ in range(R)]
    for ii in range(R):
        for jj in range(C):
            if arr[ii][jj]:
                move(ii, jj, arr[ii][jj].s, arr[ii][jj].d, arr[ii][jj].z, arr[ii][jj].s)
    arr = new_arr
    # print(arr)
    j += 1
print(answer)

