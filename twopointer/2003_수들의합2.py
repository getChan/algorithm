n, m = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

i, j = 0, 0
answer = 0
while j < n:
    cursum = sum(arr[i:j+1])
    if cursum == m:
        answer += 1
    if cursum <= m:
        j += 1
    else:
        i += 1
print(answer)