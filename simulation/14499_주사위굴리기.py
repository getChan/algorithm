class Dice(object):
    def __init__(self):
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0

    def east(self):
        self.one, self.two, self.three, self.four, self.five, self.six = \
            self.four, self.two, self.one, self.six, self.five, self.three
        
    def west(self):
        self.one, self.two, self.three, self.four, self.five, self.six = \
            self.three, self.two, self.six, self.one, self.five, self.four
        
    def north(self):
        self.one, self.two, self.three, self.four, self.five, self.six = \
            self.five, self.one, self.three, self.four, self.six, self.two
        
    def south(self):
        self.one, self.two, self.three, self.four, self.five, self.six = \
            self.two, self.six, self.three, self.four, self.one, self.five
        return self.one
    
n, m, x, y, k = [int(x) for x in input().split()]
mapp = []
for _ in range(n):
    mapp.append([int(x) for x in input().split()])
dice = Dice()
ops = [int(_) for _ in input().split()]
for op in ops:
    if op == 1 and y+1 < m:
        dice.east()
        y += 1
    elif op == 2 and y-1 >= 0:
        dice.west()
        y -= 1
    elif op == 3 and x-1 >= 0:
        dice.north()
        x -= 1
    elif op == 4 and x+1 < n:
        dice.south()
        x += 1
    else:
        continue
    
    if mapp[x][y] == 0:
        mapp[x][y] = dice.six
    else:
        dice.six = mapp[x][y]
        mapp[x][y] = 0

    print(dice.one)