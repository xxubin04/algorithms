def solution(score):
    answer = []
    avg = []
    
    for eng, math in score:
        avg.append(eng+math)
        
    avgst = sorted(avg, reverse = True) 
    
    for s in avg: 
        answer.append(avgst.index(s)+1)
    
    return answer
