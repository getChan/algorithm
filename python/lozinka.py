from sys import stdin
read = stdin.readline

n = int(read())
word = set()
for _ in range(n):
    item = read().rstrip()
    word.add(item)

    if item[::-1] in word:
        print("{} {}".format(len(item), item[(len(item)-1)//2]))
        break
    
