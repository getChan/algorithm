from sys import stdin
read = stdin.readline

words = []
for _ in range(6):
    words.append(read().rstrip())


print(words)