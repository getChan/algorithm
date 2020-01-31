n = int(input())
T, P = [], []
for _ in range(n):
    for idx, x in enumerate(input().split()):
        if not idx:
            T.append(int(x))
        else:
            P.append(int(x))

answer = 0
dp = dict() # 해당 날짜의 상담 수익
def dfs(date, cursum):
    global answer
    if answer < cursum:
        answer = cursum
    if date == n:
        return
    for i in range(date, n):
        if i+T[i] > n:
            continue
        if i+T[i] not in dp or dp[i+T[i]] < cursum+P[i]:
            dp[i+T[i]] = cursum+P[i]
            dfs(i+T[i], cursum+P[i])
        

for i in range(n):
    if i+T[i] > n:
        continue
    if i+T[i] not in dp or dp[i+T[i]] < P[i]:
        dp[i+T[i]] = P[i]
        dfs(i+T[i], P[i])
print(answer)