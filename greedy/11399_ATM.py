n = int(input())
p = [int(_) for _ in input().split()]
p.sort()
answer = 0
cur = 0
for i in p:
    cur += i
    answer += cur
print(answer)