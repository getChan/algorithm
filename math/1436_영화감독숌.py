# 6 16 26 36 46 56 61 62 63 64 65 66 ..69 76 86 96 
n = int(input())
cnt = 0
i = 0
while True:
    if '666' in (str(i)):
        cnt += 1
    if cnt == n:
        print(str(i))
        break
    i += 1

    ## 66일떄? 616 일때? 61666 / 66616