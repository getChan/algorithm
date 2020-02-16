from sys import stdin
input = stdin.readline

n, m, h = [int(x) for x in input().rstrip().split()]
ladder = [[0 for _ in range(n)] for __ in range(h)]
for _ in range(m):
    a, b = [int(x) for x in input().rstrip().split()]
    ladder[a-1][b-1] = 1


def run():
    """
    모든 i번 세로선의 결과가 i이면 True 반환
    """
    for col in range(n):
        j = col
        i = 0
        while i < h:
            if j < n and ladder[i][j]:
                j += 1
            elif j > 0 and ladder[i][j-1]:
                j -= 1
            i += 1
        if j != col:
            return False
    return True


# 모든 추가할 수 있는 가로선 개수는 3개 이하
# O((N*H)^3) 약 27000000
def add_vertical(queue=[]):
    global answer
    level = len(queue)

    if run():  # 성공하면
        if level < answer:
            answer = level
        if queue:
            i, j = queue.pop()  # 사다리 놓았던 가로줄 되돌리기
            ladder[i][j] = 0
        return

    if level == 3:  # 가로선 개수 3개이면
        i, j = queue.pop()
        ladder[i][j] = 0
        return
    # 시작 인덱스 찾기
    if queue:
        si = queue[-1][0]
    else:
        si = 0

    for i in range(si, h):
        if i == si and queue:  # 시작 인덱스 찾기
            sj = queue[-1][1]
        else:
            sj = 0
        for j in range(sj, n-1):
            if not ladder[i][j]:  # 사다리 놓여있지 않고
                if j == 0:
                    if not ladder[i][j+1]:
                        ladder[i][j] = 1
                        queue.append((i, j))
                        add_vertical(queue)
                elif j == n-1:
                    if not ladder[i][j-1]:
                        ladder[i][j] = 1
                        queue.append((i, j))
                        add_vertical(queue)
                else:
                    if not ladder[i][j-1] and not ladder[i][j+1]:
                        # 놓을 사다리가 연속해서는 안된다
                        ladder[i][j] = 1
                        queue.append((i, j))
                        add_vertical(queue)
    # 더이상 사다리 놓을 곳 없으면 되돌리기
    if queue:
        i, j = queue.pop()
        ladder[i][j] = 0
    return


answer = 4
add_vertical()

if answer == 4:
    print(-1)
else:
    print(answer)