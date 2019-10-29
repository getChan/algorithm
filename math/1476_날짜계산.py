e, s, m = [int(_) for _ in input().split()]
for i in range(1, 16*29*20):
    if i%15 == e%15\
        and i%28 == s%28\
            and i%19 == m%19:
        print(i)
        break

# 다른 사람의 풀이
e,s,m = map(int, input().split())
x = (6916*e+4845*s+4200*m) % 7980
print(x if x else 7980)