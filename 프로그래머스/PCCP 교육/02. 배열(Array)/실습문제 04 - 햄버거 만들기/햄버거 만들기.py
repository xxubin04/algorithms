def solution(ingredient):
    # 1: 빵, 2: 고기, 3: 야채
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            stack.pop(-1) for _ in range(4)
                    
    return answer
