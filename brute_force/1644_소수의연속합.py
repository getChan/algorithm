n = int(input())

prime_num = {_ for _ in range(2, n+1)}

for i in range(2, int(n**(1/2)+1)):
    if i in prime_num:
        tmp = 2
        while i*tmp <= n:
            prime_num.discard(i*tmp)
            tmp += 1

prime_num = list(prime_num)
answer = 0
start = 0
end = 0
while start < len(prime_num) and end < len(prime_num):
    if sum(prime_num[start:end+1]) < n:
        end += 1
    elif sum(prime_num[start:end+1]) > n:
        start += 1
        end = start
    else:
        answer += 1
        start += 1
        end = start

print(answer)