from sys import stdin

def digsum(arr):
    dsum = 0
    for i in arr:
        try:
            dsum += int(i)
        except ValueError:
            pass
    return (len(arr), dsum, arr) 

n = int(stdin.readline().rstrip())
serial = [stdin.readline().rstrip() for _ in range(n)]
serial.sort(key=digsum)

for i in serial:
    print(i)