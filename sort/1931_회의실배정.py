n = int(input())
time = []
for _ in range(n):
    time.append([int(__) for __ in input().split()])
# [[2,2],[1,2]] 인 경우 고려해야 한다.
time.sort(key=lambda x:[x[1],x[0]])

cnt = 0
end = 0
for t in time:
    if t[0] >= end:
        cnt += 1
        end = t[1]
print(cnt)