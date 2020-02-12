from sys import stdin
input = stdin.readline
n, m = [int(x) for x in input().rstrip().split()]
num = [int(x) for x in input().rstrip().split()]
cursum = [0]*(n+1) # cursum[i] : 처음부터 i번째까지의 합
for i in range(1, n+1):
    cursum[i] = cursum[i-1] + num[i-1]
for _ in range(m):
    s, e = [int(x) for x in input().rstrip().split()]
    print(cursum[e]-cursum[s-1])