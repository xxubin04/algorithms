def solution(cl):
    clothes = {}
    
    for c in cl:
        if (type := c[1]) in clothes.keys():
            clothes[type].append(c[0])
        else:
            clothes[type] = [c[0]]
    
    comb = 1
    for v in clothes.values():  # 각 종류마다 존재하는 의상 개수
        comb *= (len(v)+1)
    
    return comb-1