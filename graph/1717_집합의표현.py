from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
disjoint_set = [x for x in range(n+1)]

def find(s):
    if s == disjoint_set[s]:
        return s
    disjoint_set[s] = find(disjoint_set[s])
    return disjoint_set[s]

def union(s1, s2):
    s1 = find(s1)
    s2 = find(s2)
    if s1 != s2:
        disjoint_set[s2] = s1
    return

for _ in range(m):
    op, set1, set2 = [int(x) for x in input().rstrip().split()]
    if not op:
        union(set1, set2)
    else:
        if find(set1) == find(set2):
            print('YES')
        else:
            print('NO')