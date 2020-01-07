m, n = [int(x) for x in input().split()]
primes = {i for i in range(2, n+1)}
for i in range(2, 1001):
    j = i
    while j+i <= n:
        j += i
        primes.discard(j)
for p in primes:
    if p >= m:
        print(p)
        