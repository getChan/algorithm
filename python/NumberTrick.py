from sys import stdin
read = stdin.readline

x = float(read().rstrip())
flag = False
for i in range(1, 8):
    digit = 10**i
    maximum = int(digit // x)
    
    for num in range(digit//10, maximum+1):
        if (num*x)%1 == 0:
            if str(int(num*x)) == str(num)[1:]+str(num)[0]:
                print(num)
                flag = True
if not flag:
    print('No solution')
