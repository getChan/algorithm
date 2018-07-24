text = input()
max = sum(map(int, text.replace('5', '6').split()))
min = sum(map(int, text.replace('6', '5').split()))
print(min, max)

