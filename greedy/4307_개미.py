import sys
read = sys.stdin.readline
case = int(read().rstrip())

for _ in range(case):
    l, n = [int(__) for __ in read().rstrip().split()]

# 시간 = 마지막 개미의 이동거리
# 가장 빠른 시간 -> 가장 안쪽 개미가 가까운 쪽으로 떨어짐
# 가장 늦은 시간 -> 가장 바깥쪽 개미가 먼 쪽으로 떨어짐 
    fast, last = 0, 0
    for ___ in range(n):
        ant = int(read().rstrip())
        t = l-ant if l-ant < ant else  ant
        if t > fast:
            fast = t
        t = l-ant if l-ant > ant else ant
        if t > last:
            last = t
    print(fast, last)
