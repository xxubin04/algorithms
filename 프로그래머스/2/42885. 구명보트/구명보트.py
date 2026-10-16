# def solution(people, limit):
#     people.sort()
#     left, right = 0, len(people)-1
#     boats = 0
    
#     while left <= right:
#         if people[left] + people[right] <= limit:
#             left += 1
#         right -= 1
#         boats += 1
    
#     return boats
        
    
    
    
    
    
    
    
    
    
    
    

    
    


    
def solution(people, limit):
    answer = 0
    people.sort()
    s, e = 0, len(people)-1
    
    while s < e:
        total = people[s] + people[e]
        
        if total <= limit:  # 2명의 합이 제한을 넘지 않는다면
            s += 1
        
        e -= 1
            
        answer += 1
    
    if s == e:  # 1개 남음
        answer += 1
            
    return answer
    