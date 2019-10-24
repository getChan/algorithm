from itertools import permutations

k = int(input())
symbol = input().split()
mini, maxi = 10**(k+1), 0

# 최대값 : 9 ~ (9-k) / 가장 큰 수에서부터 찾아간다.
for case in permutations([str(_) for _ in range(9,8-k,-1)]):
    form = []
    i = 0 
    while i < k:
        form.append(case[i])
        form.append(symbol[i])
        i += 1
    form.append(case[-1])
    if eval(''.join(form)):
        maxi = ''.join(case)
        break
# 최소값 : 0 ~ k 로 이루어져 있다. / 가장 작은 수부터 찾아간다.
for case in permutations([str(_) for _ in range(k+1)]):
    form = []
    i = 0 
    while i < k:
        form.append(case[i])
        form.append(symbol[i])
        i += 1
    form.append(case[-1])
    if eval(''.join(form)):
        mini = ''.join(case)
        break

print(maxi)
print(mini)