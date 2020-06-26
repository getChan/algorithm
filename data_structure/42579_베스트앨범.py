from collections import Counter
def solution(genres, plays):
    counter = Counter()
    i = 0
    while i < len(genres):
        if genres[i] in counter:
            counter[genres[i]] += plays[i]
        else:
            counter[genres[i]] = plays[i]
        i += 1
    counter.most_common()