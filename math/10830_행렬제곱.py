import copy
n, b = [int(_) for _ in input().split()]
mat = []
for _ in range(n):
    mat.append([int(_) for _ in input().split()])

next_mat = copy.deepcopy(mat)
for power in range(b-1):
    i = 0
    left_mat = copy.deepcopy(next_mat)
    while i < n:
        j = 0
        while j < n:
            a = left_mat[i]
            b = []
            zi = zip(*mat)
            for _ in range(j+1):
                b = list(next(zi))
            tmp = 0
            m = 0
            while m<n:
                tmp += a[m]*b[m]
                m += 1
            next_mat[i][j] = tmp % 1000
            j += 1
        i += 1
for _ in next_mat:
    for __ in _:
        print(__, end=' ')
    print()
