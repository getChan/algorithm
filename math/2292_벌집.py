# an = 1 7 19 37 61
# bn = 6 12 18 24  =  6n 
# 인 계차수열

# 초항 1 + sigma(from 1 to n-1)  6n 
# => 1 + 3n(n-1)

n = int(input())
i = 1

while True:
    if n <= 1 + 3*i*(i-1):
        print(i)
        break
    i += 1