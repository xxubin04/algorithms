def solution(sizes):
    max_a, max_b = 0, 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        
        if a > max_a: max_a = a
        if b > max_b: max_b = b
    
    return max_a * max_b