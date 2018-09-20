def minsum(row=0, col=0, total=0):
    global minimum
    # 예외 처리
    if row+1 > len(board) or col+1 > len(board) or minimum<total :
        return
    # 기저 사례
    if row == len(board)-1 and col == len(board)-1:
        total += board[row][col]
        minimum = min(total, minimum)
        return
    total += board[row][col]
    minsum(row+1, col, total)
    minsum(row, col+1, total)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    board = [[int(x) for x in input().split()] for _ in range(n)]
    minimum = 90
    minsum()

    print('#'+str(test_case), minimum)
        
    
    # ///////////////////////////////////////////////////////////////////////////////////


