n = int(input())
i = 1
while i*i < n :
    i += 1
    if n % i == 0:
        print(n-n//i)
        break
else:
    print(n-1)
