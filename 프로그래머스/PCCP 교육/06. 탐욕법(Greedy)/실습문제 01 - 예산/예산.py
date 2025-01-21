def solution(d, budget):
    answer = 0
    total = 0
    
    for i in range(len(d := sorted(d))):
        if total + d[i] > budget:
            return i
        else:
            total += d[i]
    
    return len(d)
