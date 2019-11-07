n = int(input())
words = set()
for _ in range(n):
    words.add(input())
words = list(words)
words.sort(key=lambda x:(len(x), x))
for i in words:
    print(i)