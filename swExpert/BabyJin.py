def isTriplet(player):
    cnt = 0
    for i in player:
        if i >= 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
    else:
        return False

def isRun(player):
    if 3 in player:
        return True
    else:
        return False

T = int(input())

for t in range(1, T+1):
    cards = [int(x) for x in input().split()]
    playerone = [0 for _ in range(10)]
    playertwo = [0 for _ in range(10)]
    win = 0
    for v1, v2 in zip(cards[::2], cards[1::2]):
        playerone[v1] += 1
        playertwo[v2] += 1
        if isTriplet(playerone) or isRun(playerone):
            win = 1
            break
        elif isTriplet(playertwo) or isRun(playertwo):
            win = 2
            break
    
    print('#{}'.format(t), win)    