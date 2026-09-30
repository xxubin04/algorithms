def solution(routes):
    # 진출 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    
    answer = 0  # 필요한 카메라 개수
    idx = 0  # 현재 확인중인 경로의 인덱스
    
    while idx < len(routes):
        camera = routes[idx][1]  # 현재 카메라의 진출 시점에 카메라 설치
        
        idx += 1
        for s, e in routes[idx:]:
            if s <= camera:  # 현재 설치한 카메라에 다른 차가 잡히면
                idx += 1
            else:
                break
        answer += 1  # 카메라 개수 1 증가
    
    return answer