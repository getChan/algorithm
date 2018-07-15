from sys import stdin
from collections import deque

class Gear:
    def __init__(self, clock):
        self.clock = deque(int(x) for x in clock)

    def rotate(self, direc):
        self.clock.rotate(direc)

gears = [Gear(stdin.readline().rstrip()) for i in range(4)]

for i in range(int(stdin.readline().rstrip())):
    k, direction = map(int, stdin.readline().rstrip().split())
    k -= 1  # 톱니 객체의 인덱스값 맞춰줌
    # 톱니 돌아가는 로직부터 다시시작
    # 회전은 맞닿은 톱니가 연쇄적으로 일어남
    isrotate = [0 for x in range(4)]
    isrotate[k] = direction

    if k == 0:
        if gears[k].clock[2] != gears[k+1].clock[6]:
            isrotate[k+1] = direction*(-1)
            if gears[k+1].clock[2] != gears[k+2].clock[6]:
                isrotate[k+2] = direction
                if gears[k+2].clock[2] != gears[k+3].clock[6]:
                    isrotate[k+3] = direction*(-1)

    if k == 1:
        if gears[k-1].clock[2] != gears[k].clock[6]:
            isrotate[k-1] = direction*(-1)
        if gears[k].clock[2] != gears[k+1].clock[6]:
            isrotate[k+1] = direction*(-1)
            if gears[k+1].clock[2] != gears[k+2].clock[6]:
                isrotate[k+2] = direction

    if k == 2:
        if gears[k].clock[2] != gears[k+1].clock[6]:
            isrotate[k+1] = direction*(-1)
        if gears[k-1].clock[2] != gears[k].clock[6]:
            isrotate[k-1] = direction*(-1)
            if gears[k-2].clock[2] != gears[k-1].clock[6]:
                isrotate[k-2] = direction

    if k == 3:
        if gears[k-1].clock[2] != gears[k].clock[6]:
            isrotate[k-1] = direction*(-1)
            if gears[k-2].clock[2] != gears[k-1].clock[6]:
                isrotate[k-2] = direction
                if gears[k-3].clock[2] != gears[k-2].clock[6]:
                    isrotate[k-3] = direction*(-1)
 
    for j in range(4):
        gears[j].rotate(isrotate[j])

point = sum([(gears[x].clock.popleft())*(2**x) for x in range(4)])

print(point)
