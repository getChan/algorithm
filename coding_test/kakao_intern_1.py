import re
def solution(user_id, banned_id):
    matcheds = []
    for ban in banned_id:
        matched = []
        for user in user_id:
            # if 유저가 밴이랑 match하면
            ban.replace('*', '_')
            if re.match(ban, user):
                matched.append(user)
        matcheds.append(matched)
    print(matcheds)

    from itertools import combinations
    combinations()
    

    is_assigned = list() # room numer 저장
    answer = []
    for r in room_number:
        if r not in is_assigned:
            idx = binary_search_iter(is_assigend, r)
            is_assigned.append(r)
            answer.append(r)
            is_assigned.sort()
        else:
            idx = is_assigned.index(r)
            while True:
    
                if idx == len(is_assigned)-1 or is_assigned[idx+1] - is_assigned[idx] > 1:
                    # print(is_assigned)
                    is_assigned.append(is_assigned[idx]+1)
                    answer.append(is_assigned[idx]+1)
                    is_assigned.sort()
                    break
                idx += 1
    return answer