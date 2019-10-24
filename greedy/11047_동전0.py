# greedy
n, k = [int(_) for _ in input().split()]
coins = []
for _ in range(n):
    coins.append(int(input()))
i = len(coins)-1
cnt = 0
while k:
    if k >= coins[i]:
        cnt += k // coins[i]
        k -= (k // coins[i])*coins[i]
    else:
        i -= 1
print(cnt)
