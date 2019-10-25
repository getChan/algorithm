# N^2으로는 시간초과 난다.
# 전체 - 탈락할 사람을 세는게 낫다.
import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    points = []
    max_paper, max_interview = [100000, 100000],[100000, 100000]
    for __ in range(n):
        cur = [int(x) for x in input().rstrip().split()]
        if cur[0] < max_paper[0]:
            max_paper = cur
        if cur[1] < max_interview[1]:
            max_interview = cur
        points.append(cur)

    cnt = 0
    for p in points:
        if p[0] > max_paper[0] and p[1] > max_paper[1]:
            if p == max_paper or p == max_interview:
                continue
            cnt += 1
        elif p[1] > max_interview[1] and p[0] > max_interview[0]:
            if p == max_interview or p == max_paper:
                continue
            cnt += 1

    print(len(points)-cnt)
