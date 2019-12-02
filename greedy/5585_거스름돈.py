money = int(input())
change = 1000-money
answer = 0
while change:
    if change>=500:
        change -= 500
    elif change >= 100:
        change -= 100
    elif change >= 50:
        change -= 50
    elif change >= 10:
        change -= 10
    elif change >= 5:
        change -= 5
    else:
        change -= 1

    answer += 1
print(answer)