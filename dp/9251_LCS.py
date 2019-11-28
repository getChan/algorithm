st1 = input()
st2 = input()
dp = [[0 for _ in range(len(st1)+1)] for __ in range(len(st2)+1)]

# dp[i][j]
# 2번째 문자열의 i번째까지 문자와, 
# 1번째 문자의 j번째까지 문자의 LCS
#     A C A Y K P
#     0 0 0 0 0 0
# C 0 0 1 1 1 1 1
# A 0 1 1 2 2 2 2
# P 0 1 1 2 2 2 3
# C 0 1 2 2 2 2 3
# A 0 1 2 3 3 3 3 
# K 0 1 2 3 3 4 4
# 점화식
# dp[i+1][j+1] = dp[i][j]+1 if st1[i] == st2[j]
#              = max(dp[i+1][j], dp[i][j+1]) if st1[i] != st2[j]
for i in range(len(st2)):
    for j in range(len(st1)):
        if st2[i] == st1[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
print(dp[len(st2)][len(st1)])
