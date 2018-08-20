m, n = map(int, input().split())

cnt = 0
while m > 1 and n > 1:
    if cnt % 2 == 1:    # 홀수번쨰 curve
        n -= 1
    else:   #짝수번째 curve
        m -= 1
    cnt += 1
print(cnt+1)
