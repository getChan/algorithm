from sys import stdin
input = stdin.readline

r, c, t = [int(x) for x in input().rstrip().split()]
arr = []
for i in range(r):
    arr.append([int(x) for x in input().rstrip().split()])
    for j in range(c):
        if arr[-1][j] == -1:
            cleaner = i


def broad():  #1
    add_broad = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] >= 5:
                cnt = 0
                d = arr[i][j]//5
                for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    if not (0 <= i+di < r and 0 <= j+dj < c):
                        continue
                    if arr[i+di][j+dj] < 0:
                        continue
                    add_broad[i+di][j+dj] += d
                    cnt += 1
                arr[i][j] -= d*cnt
    for i in range(r):
        for j in range(c):
            arr[i][j] += add_broad[i][j]


def clean(cleaner): #2
    # 위쪽 청정기
    for i in range(cleaner-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for j in range(c-1):
        arr[0][j] = arr[0][j+1]
    for i in range(cleaner):
        arr[i][c-1] = arr[i+1][c-1]
    for j in range(c-1, 1, -1):
        arr[cleaner][j] = arr[cleaner][j-1]
    arr[cleaner][1] = 0

    # 아래쪽 청정기
    cleaner += 1
    for i in range(cleaner+1, r-1):
        arr[i][0] = arr[i+1][0]
    for j in range(c-1):
        arr[r-1][j] = arr[r-1][j+1]
    for i in range(r-1, cleaner, -1):
        arr[i][c-1] = arr[i-1][c-1]
    for j in range(c-1, 1, -1):
        arr[cleaner][j] = arr[cleaner][j-1]
    arr[cleaner][1] = 0


for _ in range(t):
    broad()
    clean(cleaner-1)
answer = 0
for i in range(r):
    for j in range(c):
        answer += arr[i][j]

print(answer+2)