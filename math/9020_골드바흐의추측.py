arr = [1 for _ in range(10001)]
i = 2
while i < 100:
    v = 2
    while i*v < 10000:
        arr[i*v] = 0
        v += 1
    i += 1

def goldbach():
    n = int(input())
    for i in range(n//2, n+1):
        if arr[i] == 1: # 소수이면
            for j in range(n//2, 0, -1):
                if arr[j] == 1 and i+j == n:
                    print(j, i)
                    return

t = int(input())
for _ in range(t):
    goldbach()