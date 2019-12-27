n = int(input())

def isHan(num):
    num = str(num)
    if len(num) <= 2:
        return True
    tmp = int(num[1]) - int(num[0])
    for i in range(2, len(num)):
        if tmp != int(num[i])-int(num[i-1]):
            return False
        tmp = int(num[i])-int(num[i-1])
    return True

print(len(list(filter(isHan, range(1, n+1)))))
