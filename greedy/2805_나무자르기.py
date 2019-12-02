n, m = [int(_) for _ in input().split()]
trees = [int(_) for _ in input().split()]

# n,m 값이 매우 크므로 최대 높이부터 반복문 돌리면 시간초과 날듯
# 1. 이분 탐색으로 풀어보자

right = max(trees)
left = 0

while left < right:
    mid = (left + right) // 2
    res = sum(map(lambda x:x-mid if x-mid >0 else 0 , trees))
    if res >= m:
        answer = mid
    if res == m:
        break
    elif res < m:
        right = mid
    else:
        left = mid + 1 # `+1`중요! 

print(answer)