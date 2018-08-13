from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

from fractions import Fraction

frac = Fraction(n, m)
frac = str(frac)

if frac.find('/') == -1:
    print('0')
else:
    print(abs((int(frac[-1]) - int(frac[0])) * n))