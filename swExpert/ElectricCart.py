from itertools import permutations
T = int(input())
for t in range(1, T+1):
    n = int(input())
    
    route = [[int(x) for x in input().split()] for __ in range(n)]
    perm = permutations(range(1, n))
    minimum = 2*(100*(n-1)*(n-1)+1)

    for i in perm:
        subsum = 0
        subsum += route[0][i[0]]
        subsum += route[i[-1]][0]
        for j in range(len(i)-1):
            subsum += route[i[j]][i[j+1]]
        minimum = min(subsum, minimum)

    print("#{}".format(t), minimum)