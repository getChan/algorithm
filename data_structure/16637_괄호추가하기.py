from sys import stdin
input = stdin.readline
n = int(input().rstrip())
form = input().rstrip()
# brute force
answer = -2**31

def calculate(form):
    result = []
    i = 0
    while i < len(form):
        if len(result)>=3:
            result = [eval(str(result[0])+result[1]+str(result[2]))]
        if form[i].isnumeric():
            result.append(int(form[i]))
        else:
            if form[i] == '(':
                result.append(eval(form[i+1:i+4]))
                i += 5
                continue
            else:
                result.append(form[i])
        i += 1
    if len(result) >= 3:
        result = [eval(str(result[0])+result[1]+str(result[2]))]
    return result[0]


def dfs(form, pos):
    global n, answer
    if pos >= len(form)-2:
        return
    form = form[:pos]+'('+form[pos:pos+3]+')'+form[pos+3:]
    # print(form)
    result = calculate(form)
    if result > answer:
        answer = result
    
    pos += 6
    for i in range(pos, len(form)-2, 2):
        dfs(form, i)

if n == 1:
    print(form)
else:    
    for i in range(0, n, 2):
        dfs(form, i)
    print(answer)