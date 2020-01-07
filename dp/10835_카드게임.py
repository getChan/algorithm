n = int(input())
left = [int(x) for x in input().split()]
right = [int(x) for x in input().split()]

# dp[l_index][r_index] = l_index, r_index의 경우 최대 값

# 오른쪽이 작으면 무조건 오른쪽 버리고 점수 획득
# 왼쪽이 작으면
# - 양쪽 다 버린다
# - 왼쪽 만 버린다

# 메모이제이션 방법
from sys import setrecursionlimit
setrecursionlimit(4005)

def dfs(l_index, r_index, score):
    global left, right, n, dp
    if l_index >= n or r_index >= n:
        return
    if left[l_index] > right[r_index]:
        score += right[r_index]
        if (l_index, r_index+1) in dp and score <= dp[(l_index, r_index+1)]:
            return
        else:
            dp[(l_index, r_index+1)] = score
            dfs(l_index, r_index+1, score)
    else:
        if (l_index+1, r_index+1) in dp and score <= dp[(l_index+1, r_index+1)]:
            pass
        else:
            dp[(l_index+1, r_index+1)] = score
            dfs(l_index+1, r_index+1, score)
        if (l_index+1, r_index) in dp and score <= dp[(l_index+1, r_index)]:
            return
        else:
            dp[(l_index+1, r_index)] = score
            dfs(l_index+1, r_index, score)
dp = dict()
dp[(0, 0)] = 0
dfs(0, 0, 0)

print(max(dp.values()))