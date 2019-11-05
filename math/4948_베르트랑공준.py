def search_prime(num):
    global cnt
    n = 2
    while n < num**(0.5):
        v = 2
        while v*n <= num:
            cnt[v*n] = 0
            v += 1
        n += 1
    return 

cnt = [1 for _ in range(123456*2+1)]
search_prime(123456*2)
while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
    else:
        print(sum(cnt[1+n:2*n]))

