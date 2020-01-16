T = int(input())
for t in range(1, T+1):
    N = int(input())
    names = set()
    for _ in range(N):
        names.add(input())
    names = list(names)
    names.sort(key=lambda x:(len(x), x))
    print('#{}'.format(t))
    for name in names:
        print(name)