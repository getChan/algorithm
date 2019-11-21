n = int(input())

a, b = 1, 1
for _ in range(n):
    a, b = b%10007, (2*a+b)%10007

print(a)