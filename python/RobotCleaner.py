from sys import stdin
read = stdin.readline

class Robot():
    def __init__(self, *point):
        self.row = point[0]
        self.col = point[1]
        self.direction = point[2]

    def move(self, foward=True):
        if foward:
            if self.direction == 0: #북쪽
                self.row -= 1
            elif self.direction == 3:   #서쪽
                self.col -= 1
            elif self.direction == 2: #남쪽
                self.row += 1
            else:   #동쪽
                self.col += 1
        else:
            if self.direction == 0: #북쪽
                self.row += 1
            elif self.direction == 3:   #서쪽
                self.col += 1
            elif self.direction == 2: #남쪽
                self.row -= 1
            else:   #동쪽
                self.col -= 1

    def rotate(self):
        if self.direction == 0:
            self.direction = 3
        else:
            self.direction -= 1

    def one(self):
        self.rotate()
        self.move()
        if maps[self.row][self.col] == 0:
            return True
        else:
            self.move(foward=False)
            self.rotate()
            self.rotate()
            self.rotate()
            return False

    def two(self):
        self.rotate()
        self.move()
        if maps[self.row][self.col] != 0:
            self.move(foward=False)
            return True
        else:
            self.move(foward=False)
            self.rotate()
            self.rotate()
            self.rotate()
            return False

    def three(self):
        if maps[self.row+1][self.col] != 0 and maps[self.row-1][self.col] != 0 and maps[self.row][self.col+1] != 0 and maps[self.row][self.col-1] != 0 :
            self.move(foward=False)
            return True
        else:
            return False

n, m = map(int, read().rstrip().split())
robot = Robot(*(int(x) for x in read().rstrip().split()))

maps = [[int(element) for element in read().rstrip().split()] for row in range(n)]

maps[robot.row][robot.col] = 2
while True:
    if robot.three():
        if maps[robot.row][robot.col] == 1:
            break
        continue

    if robot.two():
        continue

    if robot.one():
        maps[robot.row][robot.col] = 2
        continue
    
rst = 0
for i in maps:
    # print(i)
    rst += i.count(2)
print(rst)