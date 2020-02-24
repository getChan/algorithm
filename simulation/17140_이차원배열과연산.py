from sys import stdin
from collections import Counter
# from pprint import pprint
# print = pprint
input = stdin.readline

r, c, k = [int(x) for x in input().rstrip().split()]
r -= 1
c -= 1
arr = []
for _ in range(3):
    arr.append([int(x) for x in input().rstrip().split()])


def R():
    global arr
    max_len = len(arr[0])
    new_arr = []
    for i, seq in enumerate(arr):
        new_arr.append([])
        for idx, (num, cnt) in enumerate(sorted(Counter(seq).items(), key=(lambda x: (x[1], x[0])))):
            if num == 0:
                continue
            if idx > 50:
                break
            new_arr[i].append(num)
            new_arr[i].append(cnt)
        if len(new_arr[i]) > 100:
            new_arr[i].pop()
            new_arr[i].pop()
        if len(new_arr[i]) > max_len:
            max_len = len(new_arr[i])

    for i in range(len(new_arr)):
        add = [0]*(max_len - len(new_arr[i]))
        new_arr[i].extend(add)
    arr = new_arr


def C():
    global arr
    max_len = len(arr)
    new_arr = []
    for i, seq in enumerate(zip(*arr)):
        new_arr.append([])
        for idx, (num, cnt) in enumerate(sorted(Counter(seq).items(), key=(lambda x: (x[1], x[0])))):
            if num == 0:
                continue
            if idx > 50:
                break
            new_arr[i].append(num)
            new_arr[i].append(cnt)
        if len(new_arr[i]) > 100:
            new_arr[i].pop()
            new_arr[i].pop()
        if len(new_arr[i]) > max_len:
            max_len = len(new_arr[i])
    # print(new_arr)
    for i in range(len(new_arr)):
        add = [0]*(max_len - len(new_arr[i]))
        new_arr[i].extend(add)
    arr = list(zip(*new_arr))


time = 0
while 0<=r<len(arr) and 0<=c<len(arr[0]) and arr[r][c] != k:
    if time > 100:
        print(-1)
        break
    row_num = len(arr)
    col_num = len(arr[0])
    if row_num >= col_num:
        R()
        # print(arr)
    else:
        C()
        # print(arr)
    time += 1
else:
    print(time)