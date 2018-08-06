# 재귀함수를 이용한 permutation 함수

def permutation(iterable, n, r):
    if r == 0:
        print(iterable)
        return
    for i in range(n-1, -1, -1):
        iterable[i], iterable[i-1] = iterable[i-1], iterable[i]
        permutation(iterable, n-1, r-1)
        iterable[i], iterable[i-1] = iterable[i-1], iterable[i]

pool = ['A', 'B', 'C']
permutation(pool, 3, 1)