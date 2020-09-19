from sys import stdin
input = stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append([int(x) for x in input().rstrip().split()])

def get_minmax(window):
    