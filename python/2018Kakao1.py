from sys import stdin
read = stdin.readline

prize_1st = {1:5000000, 2:3000000, 3:2000000, 4:500000, 5:300000, 6:100000}
prize_2nd = {1:5120000, 2:2560000, 3:1280000, 4:640000, 5:320000}

t = int(read().rstrip())
for i in range(t):
    a, b = map(int, read().rstrip().split())
    if a == 3:
        a = 2
    elif a > 3 and a <= 6:
        a = 3
    elif a > 6 and a <= 10:
        a = 4
    elif a > 10 and a <= 15:
        a = 5
    elif a > 15 and a <= 21:
        a = 6

    if b == 3:
        b = 2
    elif b > 3 and b <= 7:
        b = 3
    elif b > 7 and b <= 15:
        b = 4
    elif b > 15 and b <= 31:
        b = 5

    print(prize_1st.get(a, 0) + prize_2nd.get(b, 0))
