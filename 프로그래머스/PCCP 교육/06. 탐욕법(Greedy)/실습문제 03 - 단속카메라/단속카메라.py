def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    answer = 0
    last_camera = -float('inf')
    
    for start, end in routes:
        if start > last_camera:
            answer += 1
            last_camera = end;
    return answer 
