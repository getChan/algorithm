# n, k = [int(_) for _ in input().split()]
# n C k = n+1 C k+1 - n C k+1
# n C k = n C n-k
import timeit

for _ in range(40000000):
    pass