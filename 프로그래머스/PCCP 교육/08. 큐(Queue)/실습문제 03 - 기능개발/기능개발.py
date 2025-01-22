from collections import deque
import math as m

def solution(progresses, speeds):
    spend_time = deque()
    answer = []
    for p in range(len(progresses)):
        spend_time.append(m.ceil((100 - progresses[p]) / speeds[p]))

    max_time = spend_time[0] 
    cnt = 0
    
    for time in spend_time:
        if time > max_time:
            answer.append(cnt)
            cnt = 1
            max_time = time 
        else:
            cnt += 1 
    
    answer.append(cnt)
    
    return answer
