k = int(input())
inequals = input().split()
max_answer = '0000000000' 
min_answer = '9999999999'
def dfs(arr):
    global max_answer, min_answer
    n = len(arr)
    if n > k:
        result = int(''.join(map(str,arr)))
        if result > int(max_answer):
            max_answer = ''.join(map(str,arr))
        if result < int(min_answer):
            min_answer = ''.join(map(str,arr))
        return
    it = list(range(10))
    for i in arr:
        it.remove(i)
    
    for i in it:
        if eval(str(arr[-1])+inequals[n-1]+str(i)):
            dfs(arr+[i])

for i in range(10):
    dfs([i])
print(max_answer)
print(min_answer)