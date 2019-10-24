t = int(input())
for i in range(t):
    n = int(input())
    line = [0 for _ in range(5000)]
    for j in range(n):
        a, b = [int(x) for x in input().split()]
        for v in range(a-1, b):
            line[v] += 1
    p = int(input())
    
    output = '#'+str(i+1)
    for j in range(p):
        c = int(input())
        output += ' '+str(line[c-1])
    print(output)
