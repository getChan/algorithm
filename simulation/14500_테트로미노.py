from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
paper = []
for _ in range(n):
    paper.append([int(x) for x in input().rstrip().split()])

# 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값 구하기
# 테트로미노는 하나만 놓는다.
# 모든 칸에 대해 가능한 테트로미노를 모두 놓아 본다.
# 약 O(N*M) ~= 250000*alpha
answer = 0
for i in range(n):
    for j in range(m):
        if j+3 < m:
            answer = max(answer, sum(paper[i][j:j+4]))
        if i+3 < n:
            answer = max(answer, paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+3][j])
        if i+1 < n and j+1 < m:
            tmp = paper[i][j]+paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1]
            answer = max(answer, tmp)
        if i+2 < n and j+1 < m:
            tmp = paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j+1]
            tmp = max(tmp, paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j])
            answer = max(answer, tmp)
        if i+1 < n and j+2 < m:
            tmp = paper[i+1][j]+paper[i+1][j+1]+paper[i][j+1]+paper[i][j+2]
            tmp = max(tmp, paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i+1][j+2])
            answer = max(answer, tmp)
        if i+2 < n and j+1 < m:
            tmp = paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+2][j+1]
            tmp = max(tmp, paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i+2][j+1])
            tmp = max(tmp, paper[i][j+1]+paper[i+1][j+1]+paper[i+2][j]+paper[i+2][j+1])
            tmp = max(tmp, paper[i][j]+paper[i][j+1]+paper[i+1][j]+paper[i+2][j])
            answer = max(answer, tmp)
        if i+1 < n and j+2 < m:
            tmp = paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+1][j+2]
            tmp = max(tmp, paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i+1][j+2])
            tmp = max(tmp, paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i+1][j])
            tmp = max(tmp, paper[i][j+2]+paper[i+1][j+2]+paper[i+1][j]+paper[i+1][j+1])
            answer = max(answer, tmp)
        if i+1 < n and j+2 < m:
            tmp = paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i+1][j+1]
            tmp = max(tmp, paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1]+paper[i+1][j+2])
            answer = max(answer, tmp)
        if i+2 < n and j+1 < m:
            tmp = paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j]
            tmp = max(tmp, paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j+1])
            answer = max(answer, tmp)

print(answer)