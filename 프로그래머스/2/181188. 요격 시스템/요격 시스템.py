def solution(targets):
    # (끝, 시작) 좌표 오름차순으로 정렬
    answer = 0
    l = len(targets)
    targets.sort(key=lambda x: (x[1], x[0]))
    cnt = 0
    idx = 0  # 기준이 되는 미사일 인덱스
    
    while cnt < len(targets):  # 다 요격할 때까지
        std = targets[idx][1]
        
        for i in range(idx, l):
            if targets[i][0] < std:  # 다른 미사일들 중에서 시작점이 기준점보다 작은 경우에만 같이 요격가능
                cnt += 1
            else:
                idx = i  # 요격이 안되는 지점으로 갱신
                break
            
        answer += 1

    return answer