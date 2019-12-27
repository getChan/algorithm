n = int(input())
# dp[i] : i자리 이친수의 개수
# dp[1]=1, dp[2]= 1
# dp[i+2] = dp[i] + dp[i+1]
a, b = 1, 1
for i in range(n-1):
    a, b = b, a+b
print(a)