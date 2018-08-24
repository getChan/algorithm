from sys import stdin

read = stdin.readline

n = int(read().rstrip())
num = list(map(int, read().rstrip().split()))
answer = num[-1]
num = num[:-1]
cnt = 0
#memo =
#메모이제이션 기법 적용하기
def addNode(num, subtotal):
    global cnt
    subtotal += num[0]
    
    if subtotal < 0 or subtotal > 20:
        return
    if len(num) == 1:
        if subtotal == answer:
            cnt += 1
        return
    addNode(num[1:], subtotal)
    subtractNode(num[1:], subtotal)
    
def subtractNode(num, subtotal):
    global cnt
    subtotal -= num[0]
    
    if subtotal < 0 or subtotal > 20:
        return
    if len(num) == 1:
        if subtotal == answer:
            cnt += 1
        return
    addNode(num[1:], subtotal)
    subtractNode(num[1:], subtotal)

subtotal = num[0]
addNode(num[1:], subtotal)
subtractNode(num[1:], subtotal)
print(cnt)

