# from collections import Counter

# def solution(k, tangerine):
#     count = Counter(tangerine)   
#     sorted_counts = sorted(count.values(), reverse=True) 
    
#     result = 0
#     for c in sorted_counts:
#         k -= c
#         result += 1
#         if k <= 0:
#             break
    
#     return result




from collections import Counter 

def solution(k, tangerine):
    t_counter = Counter(tangerine)
    t = sorted(t_counter.items(), key=lambda x: -x[1])
    
    total = 0
    for idx, pair in enumerate(t):
        if total < k:
            total += pair[1]
        else:
            return idx
    
    return len(t)








