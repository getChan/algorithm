l, c = [int(x) for x in input().split()]
chars = input().split()
chars.sort()
mo = {'a', 'e', 'i', 'o', 'u'}
def dfs(ch_idx, string, ja_cnt, mo_cnt):
    if chars[ch_idx] in mo:
        mo_cnt += 1
    else:
        ja_cnt += 1
    string += chars[ch_idx]

    if len(string) == l:
        if ja_cnt >= 2 and mo_cnt >= 1:
            print(string)
        return
    
    for next_idx in range(ch_idx+1, c-(l-len(string))+1):
        dfs(next_idx, string, ja_cnt, mo_cnt)

for start_idx in range(c-l+1):
    dfs(start_idx, '', 0, 0)