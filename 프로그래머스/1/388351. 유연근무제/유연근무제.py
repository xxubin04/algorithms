def solution(schedules, timelogs, startday):
    ans = (num := len(timelogs))  # 전체 인원 수로 초기화 
    valid_person = [1] * num  # 아직 지각하지 않은 직원들 정보 저장
    
    for i in range(num):
        time = schedules[i]
        schedules[i] = (time // 100) * 60 + (time % 100)
        for j in range(7):
            time = timelogs[i][j]
            timelogs[i][j] = (time // 100) * 60 + (time % 100)
        
    day = startday - 1
    for d in range(7):
        day += 1
        
        for p in range(num):
            if valid_person[p] == 0:  # 이미 지각한 사람이라면 
                continue 
                
            if day % 7 == 6 or day % 7 == 0:  # 토요일/일요일
                continue 
        
            # 10분 초과라면 
            if timelogs[p][d] > schedules[p] + 10:
                ans -= 1
                valid_person[p] = 0
    
    return ans
                