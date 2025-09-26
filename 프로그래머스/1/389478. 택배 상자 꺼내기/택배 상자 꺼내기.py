def solution(n, w, num):
    arg = []
     
    stack = False  # 위에 쌓이는지 여부
    x, y = -1, -1
    
    for i in range(n // w):
        if i * w + 1 <= num < (i + 1) * w + 1:
            if i % 2 == 0:  # 오른쪽으로 쌓음 
                x, y = i, num - (i * w + 1)
            else:
                x, y = i, w - (num - (i * w))
            stack = True
            answer = 0
        
        if not stack:
            continue 
        else:
            answer += 1
    
    if x == -1:
        return 1
    
    if n % w != 0:
        if (n // w) % 2 == 0 and n % w - 1 >= y:  # 상자를 오른쪽으로 쌓아야 한다면
            answer += 1
        elif (n // w) % 2 == 1 and w - (n % w) <= y:  # 상자를 왼쪽으로 쌓아야 한다면
            answer += 1
    
    return answer