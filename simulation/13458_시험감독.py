from sys import stdin
input = stdin.readline

n = int(input().rstrip())
arr = [int(x) for x in input().rstrip().split()]
b, c = [int(x) for x in input().rstrip().split()]

answer = 0
for a in arr:
    answer += 1
    if a < b:
        continue
    else:
        if (a-b) % c == 0:
            answer += (a-b)//c
        else:
            answer += (a-b)//c + 1
print(answer)