from sys import stdin
input = stdin.readline

n = int(input().rstrip())
num = [int(x) for x in input().rstrip().split()]

for _ in range(int(input().rstrip())):
    s, e = [int(x) for x in input().rstrip().split()]
    s -= 1
    e -= 1
    if (e-s)%2:
        print(0)
    else:
        if num[s:(s+e)//2] == num[(s+e)//2+1:e+1]:
            print(1)
        else:
            print(0)

