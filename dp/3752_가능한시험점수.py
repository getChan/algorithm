for t in range(1, int(input())+1):
    n = int(input())
    scores = [int(x) for x in input().split()]
    dp = [False for _ in range(sum(scores)+1)]
    dp[0] = True
    # dp[i] : i가 받을 수 있는 점수이면 True
    for score in scores:
        for i in range(len(dp)-1, -1, -1):
            if dp[i]: # i는 더할 수 있는 점수
                dp[i+score] = True
    print('#{}'.format(t), sum(dp))