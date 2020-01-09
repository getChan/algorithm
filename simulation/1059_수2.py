l = int(input())
lset = [int(x) for x in input().split()]
n = int(input())
lset.append(0)
lset.sort()

i = 0
while i < l:
    if lset[i] < n and lset[i+1] > n:
        print((n-lset[i]-1)*(lset[i+1]-n) + lset[i+1]-n-1)
        break
    elif lset[i] >= n:
        print(0)
        break
    i += 1
else:
    print(0)