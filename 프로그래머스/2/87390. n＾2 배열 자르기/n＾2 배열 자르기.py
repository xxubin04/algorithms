def solution(n, left, right):
    result = []
    
    for i in range(left, right+1):
        x, y = i//n, i%n
        result.append(max(x, y)+1)
    
    return result