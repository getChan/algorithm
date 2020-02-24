n = [int(x) for x in input().split()]

class Node(object):
    def __init__(self, point, child):
        self.point = point
        self.child = None

start_node = Node(0, Node)


horses = [0, 0, 0, 0]
scores = [0, 0, 0, 0]

for i in range(4):
    n[i]