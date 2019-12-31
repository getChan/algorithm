# 12345678     9
# dp[i] : i자리수인 수의 계단수의 개수
# dp[1] = 9
# dp[2] = 17
# dp[3] = (dp[2]-2)*2 + 2
# dp[i] = (dp[i-1]-2i)*2 + 2i
n = int(input())
num  = 17
for i in range(n-2):
    num = (num-2*(i+1))*2 + 2*(i+1) % 1000000000
if n == 1:
    print(1)
else:
    print(num)