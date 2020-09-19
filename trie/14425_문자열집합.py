n, m = [int(x) for x in input().split()]

root = dict()
for _ in range(n):
    node = root
    for ch in input().rstrip():
        if ch not in node:
            node[ch] = dict()
        node = node[ch]
answer = 0
for _ in range(m):
    node = root
    for ch in input().rstrip():
        if ch not in node:
            break
        node = node[ch]
    else:
        if not node:
            answer += 1
print(answer)


