t = int(input())

for i in range(t):
    d, a, b, f = [int(x) for x in input().split()]
    t = d / (a+b) * f
    print('#'+str(i), t)
