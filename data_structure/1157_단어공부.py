from collections import Counter

counter = Counter(input().upper())
most = counter.most_common(2)
if len(most) == 1:
    print(most[0][0])
    exit()
if most[0][1] == most[1][1]:
    print('?')
else:
    print(most[0][0])
