to_visit = {i for i in range(1,10001)}
def search(n, start=True):
    while n <= 10000:
        if n not in to_visit:
            return
        else:
            if not start:
                to_visit.discard(n)
            n = n + sum(map(int, str(n)))
            start = False
            

for i in range(1,10000):
    if i in to_visit:
        search(i)

for i in to_visit:
    print(i)