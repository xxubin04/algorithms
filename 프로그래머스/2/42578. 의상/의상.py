def solution(cl):
    answer = 1
    clothes = {}
    
    for c in cl:
        if c[1] in clothes:
            clothes[c[1]].append(c[0])
        else:
            clothes[c[1]] = [c[0]]
        
    for v in clothes.values():
        answer *= (len(v)+1)
    
    return answer - 1  # 아무것도 안 입는 경우(1) 빼기