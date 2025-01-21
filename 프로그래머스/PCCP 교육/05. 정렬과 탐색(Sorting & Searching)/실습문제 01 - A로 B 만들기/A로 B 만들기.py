def solution(before, after):
    b_list = sorted(list(before))
    a_list = sorted(list(after))
    
    if b_list == a_list:
        return 1
    else:
        return 0
