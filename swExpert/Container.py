T = int(input())

for t in range(1, T+1):
    n, m = (int(x) for x in input().split())
    weight = [int(x) for x in input().split()]
    vol = [int(x) for x in input().split()]
    
    total = 0
    cnt = 0
    weight.sort(reverse=True)
    vol.sort(reverse=True)
    for v in vol:
        for i, w in enumerate(weight):
            if w <= v:
                total += w
                del weight[:i+1]
                break
            
    print("#{}".format(t), total)
    