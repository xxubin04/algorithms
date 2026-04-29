from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)   
    sorted_counts = sorted(count.values(), reverse=True) 
    
    result = 0
    for c in sorted_counts:
        k -= c
        result += 1
        if k <= 0:
            break
    
    return result