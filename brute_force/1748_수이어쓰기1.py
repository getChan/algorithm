# (9-1+1)*1 + (99-10+1)*2 + (999-100+1)*3

n = input()
answer = 0
for i in range(1, len(n)):
    answer += (10**i-10**(i-1))*i
answer += (int(n)-10**(len(n)-1)+1)*len(n)
print(answer)