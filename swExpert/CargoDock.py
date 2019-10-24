T = int(input())

for t in range(1, T+1):
    n = int(input())
    time = list()
    for _ in range(n):
        time.append(tuple(int(x) for x in input().split()))
    time.sort(key=lambda x: x[1])
    cnt = 0
    tmp = time
    while time:
        p = time[0]
        end = p[1]
        time = list(filter(lambda x: x[0] >= end, time))
        cnt += 1
        
        
    print("#{}".format(t), cnt)
