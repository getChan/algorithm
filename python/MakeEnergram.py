from sys import stdin

# words = list()

# for _ in range(2):
#     d = {}
#     word = stdin.readline().rstrip()
#     for i in word:
#         d[i]=word.count(i)
#     words.append(d)

# cnt = 0

# wordset = (words[0].items() | words[1].items())

# for i in wordset:
#     cnt += i[1]

# intersectset = words[0].keys() & words[1].keys()
# for i in intersectset:
#     if words[0][i] == words[1][i]:
#         cnt -= words[0][i]
#     else:
#         cnt -= words[0][i] + words[1][i]
#         cnt += abs(words[0][i] - words[1][i])
# print(cnt)

word1 = stdin.readline().rstrip()
word2 = stdin.readline().rstrip()

wordset = set(word1+word2)
cnt = 0
for i in wordset:
    cnt += abs(word1.count(i)-word2.count(i))

print(cnt)
