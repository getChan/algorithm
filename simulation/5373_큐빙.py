from sys import stdin
input = stdin.readline


class Cube(object):
    def __init__(self):
        self.U = [['w' for _ in range(3)] for __ in range(3)]
        self.D = [['y' for _ in range(3)] for __ in range(3)]
        self.F = [['r' for _ in range(3)] for __ in range(3)]
        self.B = [['o' for _ in range(3)] for __ in range(3)]
        self.L = [['g' for _ in range(3)] for __ in range(3)]
        self.R = [['b' for _ in range(3)] for __ in range(3)]

    def rotate(self, face, direction):
        if face == 'U':
            if direction == '+':
                self.L[0], self.B[0], self.R[0], self.F[0] = \
                    self.F[0].copy(), self.L[0].copy(), self.B[0].copy(), self.R[0].copy()
            else:
                self.R[0], self.F[0], self.L[0], self.B[0] = \
                    self.F[0].copy(), self.L[0].copy(), self.B[0].copy(), self.R[0].copy()

        elif face == 'D':
            if direction == '+':
                self.R[2], self.F[2], self.L[2], self.B[2] = \
                    self.F[2].copy(), self.L[2].copy(), self.B[2].copy(), self.R[2].copy()
            else:
                self.L[2], self.B[2], self.R[2], self.F[2] = \
                    self.F[2].copy(), self.L[2].copy(), self.B[2].copy(), self.R[2].copy()

        elif face == 'F':
            if direction == '+':
                for i in range(3):
                    self.R[i][0], self.U[2][i], self.L[i][2], self.B[0][i] =\
                        self.U[2][i], self.L[i][2], self.B[0][i], self.R[i][0]
            else:
                for i in range(3):
                    self.L[i][2], self.U[2][i], self.R[i][0], self.B[0][i] =\
                        self.U[2][i], self.R[i][0], self.B[0][i], self.L[i][2]

        elif face == 'B':
            if direction == '+':
                for i in range(3):
                    self.L[i][0], self.U[0][i], self.R[i][2], self.B[0][i] =\
                        self.U[0][i], self.R[i][2], self.B[2][i], self.R[i][0]
            else:
                for i in range(3):
                    self.L[i][2], self.U[2][i], self.R[i][0], self.B[0][i] =\
                        self.U[2][i], self.R[i][0], self.B[0][i], self.L[i][2]


for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    ops = [x for x in input().rstrip().split()]
