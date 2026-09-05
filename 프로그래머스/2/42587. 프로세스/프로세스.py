from collections import deque

def solution(priorities, location):
    q = deque(list(enumerate(priorities)))
    priorities.sort()  # 오름차순으로 정렬
    answer = []
    
    while q:
        idx, p = q.popleft()
        
        if p != priorities[-1]:  # 최댓값이 아니라면
            q.append((idx, p))
            continue
        
        answer.append(idx)
        priorities.pop()
        
    return answer.index(location) + 1
        
        
    
#     q = deque(priorities)
#     max_p = max(priorities)
#     loc = location
#     cnt = 0
    
#     while True:
#         now_p = q.popleft()
        
#         if now_p < max_p:
#             q.append(now_p)
            
#             if loc == 0:
#                 loc = len(q) - 1
#             else:
#                 loc -= 1
#         else:
#             cnt += 1
#             if loc == 0:
#                 return cnt
            
#             loc -= 1
            
#             if q:
#                 max_p = max(q)
                