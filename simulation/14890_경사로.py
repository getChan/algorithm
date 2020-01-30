from sys import stdin
input = stdin.readline

n, l = [int(_) for _ in input().rstrip().split()]
mapp = []
for _ in range(n):
    mapp.append([int(x) for x in input().rstrip().split()])

answer = 0

for row in range(n):
    flat = 1
    for i in range(1, n):
        if not (0 <= abs(mapp[row][i]-mapp[row][i-1]) <= 1):
            break
        if mapp[row][i-1] == mapp[row][i]:
            flat += 1
        else:
            if flat < l:
                break
            flat = 1
    else:
        answer += 1

for col in range(n):
    flat = 1
    for i in range(1, n):
        if not (0 <= abs(mapp[i][col]-mapp[i-1][col]) <= 1):
            break

        if mapp[i-1][col] == mapp[i][col]:
            flat += 1
        else:
            if flat < l:
                break
            flat = 1
    else:
        answer += 1

print(answer)