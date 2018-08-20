from sys import stdin
read = stdin.readline

words = []
for _ in range(6):
    words.append(read().rstrip())
words.sort()

rst = []

spell_0 = [x[0] for x in words]
spell_1 = [x[1] for x in words]
spell_2 = [x[2] for x in words]
for word in words:
    if spell_0.count(word[0]) > 0 and spell_0.count(word[1]) > 0 and spell_0.count(word[2]) > 0:
        rst.append(word)
        words.remove(word)
        break

spell_0 = [x[0] for x in words]
spell_1 = [x[1] for x in words]
spell_2 = [x[2] for x in words]
for word in words:
    if spell_1.count(word[0]) > 0 and spell_1.count(word[1]) > 0 and spell_1.count(word[2]) > 0:
        rst.append(word)
        words.remove(word)
        break

spell_0 = [x[0] for x in words]
spell_1 = [x[1] for x in words]
spell_2 = [x[2] for x in words]
for word in words:
    if spell_2.count(word[0]) > 0 and spell_2.count(word[1]) > 0 and spell_2.count(word[2]) > 0:
        rst.append(word)
        words.remove(word)
        break

print(rst)