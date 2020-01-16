from sys import stdin
input = stdin.readline
T = int(input().rstrip())

def find(username):
    if username in disjoint_set:
        if disjoint_set[username] == username:
            return username
        else:
            disjoint_set[username] = find(disjoint_set[username])
            return disjoint_set[username]
    else:
        disjoint_set[username] = username
        cnt[username] = 1
        return username

def union(user1, user2):
    user1 = find(user1)
    user2 = find(user2)

    if user1 != user2: # 다른 집합에 있다
        disjoint_set[user2] = user1
        cnt[user1] += cnt[user2]

for _ in range(T):
    F = int(input().rstrip())
    disjoint_set = dict() # key : 사용자 - value : 부모노드
    cnt = dict() # 사용자 친구의 수
    for __ in range(F):
        user1, user2 = input().rstrip().split()
        union(user1, user2)
        print(cnt[find(user1)])