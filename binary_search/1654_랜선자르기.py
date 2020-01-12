# N개 랜선을 무조건 만들 수 있다.
# 자투리 랜선을 합쳐서 새로운 랜선 만들 수 없다.
# cm단위로 반복해서 자른다고 하면 2^31 번 반복해야 한다
# 이진 탐색으로 시도해보자

from sys import stdin
input = stdin.readline
k, n = [int(x) for x in input().rstrip().split()]
lan = []
for _ in range(k):
    lan.append(int(input().rstrip()))
top, bottom = 2**31-1, 1
while bottom <= top:
    mid = (bottom+top) // 2
    if sum(map(lambda x:x//mid, lan)) >= n:
        answer = mid
        bottom = mid+1
    else:
        top = mid-1
    
print(answer)
