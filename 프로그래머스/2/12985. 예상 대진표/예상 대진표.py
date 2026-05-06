def solution(n,a,b):
    r = 0
    
    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        r += 1
        
    return r