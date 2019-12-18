n = int(input())
numbers = {int(x) for x in input().split()}
prime = {i for i in range(2,1001)}
for i in range(2, 34):
    k = 2
    while i*k <= 1000:
        prime.discard(i*k)
        k += 1
        
print(len(numbers&prime))