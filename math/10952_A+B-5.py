while True:
    a, b = [int(x) for x in input().split()]
    if a==0 and b==0:
        break
    print(a+b)