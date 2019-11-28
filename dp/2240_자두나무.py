t, w = [int(_) for _ in input().split()]
cont = []
before_tree = 1
stack = 0
for _ in range(t):
    cur_tree = int(input())
    if before_tree == cur_tree:
        stack += 1
    else:
        cont.append(stack)
        stack = 1
    before_tree = cur_tree
cont.append(stack)
# cont : 연속해서 떨어지는 자두의 수
i = 0
while i<len(cont):
    
    i += 2
    


# dp = [0 for _ in range(t)]
# dp[i] : i번 움직일 떄 최대 개수
# dp[i+1] = dp[i] + max(count(1), count(2))
# 1 2 3 4 5
# 4 4 6 7