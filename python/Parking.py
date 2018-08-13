from sys import stdin
read = stdin.readline

a, b, c = map(int, read().rstrip().split())
timeinfo = list()
for _ in range(3):
    timeinfo.append(tuple(map(int, read().rstrip().split())))

# 주차되어있는 차의 수
cnt = 0
fee = 0
time = 0
arrive, depart = zip(*timeinfo)
while time < max(depart) :
    time += 1
    
    cnt += arrive.count(time)
    cnt -= depart.count(time)

    if cnt == 1:
        fee += a
    elif cnt == 2:
        fee += cnt*b
    elif cnt == 3:
        fee += cnt*c

print(fee)
