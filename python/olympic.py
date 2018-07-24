from sys import stdin
from operator import itemgetter
read = stdin.readline

n, k = map(int, read().rstrip().split())
data = list()
for i in range(n):
    key, gold, silver, bronze = map(int, read().rstrip().split())

    data.append({'key':key, 'gold':gold, 'silver':silver, 'bronze':bronze})

data.sort(key=itemgetter('gold','silver','bronze'), reverse=True)

cnt = 1
flag = 0
temp = (data[0]['gold'], data[0]['silver'], data[0]['bronze'])
if n == 1:
    print("1")
if data[0]['key'] == k:
    print("1")
for i in data[1:]:
    cnt += 1
    next = (i['gold'], i['silver'], i['bronze'])
    if temp == next:
        cnt -= 1
        flag += 1
    else:
        cnt += flag
        flag = 0
    
    if i['key'] == k:
        print(cnt)
    temp = next