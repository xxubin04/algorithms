def solution(progresses, speeds):
    time = []
    answer = []
    
    for p, s in zip(progresses, speeds):
        if (cal := (100 - p)) % s == 0:  # 나누어 떨어진다면
            time.append(cal // s)
        else:
            time.append(cal // s + 1)  # 나누어 떨어지지 않는다면 
    
    std = time[0]  # 배포 시기에 가장 앞에 위치한 기능의 필요한 시간
    cnt = 1  # 한 번에 배포될 수 있는 개수
    for i in range(1, len(time)):
        if time[i] <= std:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            std = time[i]
    
    answer.append(cnt)
    return answer
    