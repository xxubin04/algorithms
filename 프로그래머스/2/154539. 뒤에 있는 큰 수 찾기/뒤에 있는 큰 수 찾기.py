def solution(numbers):
    l = len(numbers)
    answer = [-1] * l
    stack = []
    
    for idx in range(l-1, -1, -1):
        
        while stack:
            if stack[-1] <= numbers[idx]:  # 뒤에 있는 최댓값이 현재값보다 작다면
                stack.pop()
            else:  # 최댓값을 발견했다면
                answer[idx] = stack[-1]
                break
        
        stack.append(numbers[idx])
        
    return answer
                
    
#     answer = deque()
#     l = len(numbers)
#     max_value = 0 
    
#     for idx1 in range(l-1, -1, -1):
#         # 현재 값보다 큰 값이 없다면
#         if (n := numbers[idx1]) >= max_value:  # 최댓값 갱신
#             max_value = numbers[idx1]
#             answer.appendleft(-1)  # -1 추가
#         elif n < max_value:  # 최댓값이 더 크다면
#             answer.appendleft(max_value)  # 최댓값 추가 
    
#     return list(answer)
    
#     for idx1 in range(l):
#         find_bigger = False
#         for idx2 in range(idx1+1, l):
#             if numbers[idx1] < (n := numbers[idx2]):
#                 answer.append(n)
#                 find_bigger = True
#                 break
        
#         if not find_bigger:
#             answer.append(-1)        
    
#     return answer