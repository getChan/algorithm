from itertools import permutations

n = int(input())
arr = [int(_) for _ in input().split()]
answer = 0
for form in permutations(arr):
    tmp = 0
    for i in range(1, n):
        tmp += abs(form[i-1]-form[i])
    if tmp > answer:
        answer = tmp
print(answer)