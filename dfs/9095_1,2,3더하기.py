def dfs(subsum, target):
    global answer
    if subsum == target:
        answer += 1
        return
    elif subsum > target:
        return
    dfs(subsum+1, target)
    dfs(subsum+2, target)
    dfs(subsum+3, target)


for _ in range(int(input())):
    n = int(input())
    answer = 0
    dfs(0, n)
    print(answer)
