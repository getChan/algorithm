n, r, c =[int(_) for _ in input().split()]
cnt = 0
# index가 1에서 시작한다고 가정


def search(n, r, c, m):
    global cnt
    if n < 0:
        cnt += 2**m
        print(cnt)
        return
    if r <= 2**(n-1) and c <= 2**(n-1):
        search(n-1, r//2, c//2, n-2)
    cnt += 2**m
    if r <= 2**(n-1) and c > 2**(n-1):
        search(n-1, r//2, c//2, n-2)
    cnt += 2**m
    if r > 2**(n-1) and c <= 2**(n-1):
        search(n-1, r//2, c//2, n-2)
    cnt += 2**m
    if r > 2**(n-1) and c > 2**(n-1):
        search(n-1, r//2, c//2, n-2)
    

r += 1
c += 1
search(n, r, c, n)
