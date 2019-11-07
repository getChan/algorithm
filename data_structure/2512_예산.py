n = int(input())
budgets = [int(_) for _ in input().split()]
m = int(input())
i = 0
budgets.sort()
for b in budgets:
    div = m//n
    if b < div:
        m -= b
        n -= 1
    else:
        print(div)
        break
else:
    print(budgets[-1])