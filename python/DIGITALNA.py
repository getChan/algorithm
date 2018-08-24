from sys import stdin
read = stdin.readline

n = int(read().rstrip())
channels = []
for i in range(n):
    channels.append(read().rstrip())

index_1, index_2 = channels.index('KBS1'), channels.index('KBS2')

if index_1 > index_2 and index_2 != 0 :
    print('1'*index_1+'4'*index_1+'1'*(index_2+1)+'4'*index_2)
else:
    print('1'*index_1+'4'*index_1+'1'*index_2+'4'*(index_2-1))
