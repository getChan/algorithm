from sys import stdin
input = stdin.readline
n, s = [int(x) for x in input().rstrip().split()]
arr = [int(x) for x in input().rstrip().split()]

answer = n+1
i, j = 0, 0
cursum = arr[i]
while j < n:
    if cursum < s:
        j += 1
        if j == n:
            break
        cursum += arr[j]
        if j+1-i >= answer:
            cursum -= arr[i]
            i += 1
    else:
        answer = min(answer, j+1-i)
        cursum -= arr[i]
        i += 1
if answer > n:
    print(0)
else:
    print(answer)