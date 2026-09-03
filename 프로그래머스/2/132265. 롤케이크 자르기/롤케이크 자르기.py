from collections import Counter

def solution(topping):
    answer = 0
    a = set()
    b = Counter(topping)
    
    for i in topping:
        a.add(i)
        b[i] -= 1
        
        if b[i] == 0:
            del b[i]
        
        if len(a) == len(b):
            answer += 1
    
    return answer
        