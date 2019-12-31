# greedy로 풀어보기
# n = int(input())
# price_per_card = [int(x)/(i+1) for i, x in enumerate(input().split())]
# answer = 0
# while n:
#     most = (0, 0)
#     for i in range(n):
#         if price_per_card[i] > most[-1]:
#             most = (i+1 , price_per_card[i])
#     answer += int(n//most[0]*(most[0]*most[1]))
#     n -= n//most[0]*most[0]
# print(answer)
    
# dp로 풀어보기
n = int(input())
price = [int(x) for x in input().split()]
