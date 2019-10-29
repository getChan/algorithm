# import string
# word = input()
# word_set = {ch for ch in word}
# for ch in string.ascii_lowercase:
#     if ch not in word_set:
#         print(-1, end=' ')
#     else:
#         print(word.index(ch), end=' ')


## 더 빠른 방법
import string
wordict = {_:-1 for _ in string.ascii_lowercase}
word = input()
word_len = len(word)
for idx, ch in enumerate(word[::-1]):
    wordict[ch] = word_len -1 - idx
print(*wordict.values())