n, m, k = [int(_) for _ in input().split()]

# 2m == n 이 되도록 만들면 최대로 팀(n개)을 만들 수 있다.

while k:
    if n >= 2*m-1:
        n -= 1
    else:
        m -= 1
    k -= 1

if n <= 1 or m <= 0: # 절대 안되는 조건들, 음수 예외처리
    print(0)
    exit(0)

if n >= 2*m:
    print(m)
else:
    print(n//2)
