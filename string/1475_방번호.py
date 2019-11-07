n = input()
numbers = [0 for _ in range(10)]
for ch in n:
    if ch == '6' or ch == '9':
        if numbers[6] > numbers[9]:
            numbers[9] += 1
        else:
            numbers[6] += 1
    else:
        numbers[int(ch)] += 1
print(max(numbers))
