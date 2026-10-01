from collections import deque

def solution(places):
    answer = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(x, y, dst):
        nonlocal room
        
        q = deque([(x, y, dst)])
        visited = [[0] * 5 for _ in range(5)]
        
        while q:
            x, y, dst = q.popleft()  # 행, 열, 거리
            visited[x][y] = 1  # 방문 처리
            
            if dst == 2:  # 이전 거리가 2라면 이제 더 이상 확인 안해도 됨
                continue
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                # 범위 안이면서 아직 방문하지 않은 곳
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] != 1:
                    
                    # 다른 응시자와의 거리가 3 미만이면
                    if room[nx][ny] == "P":
                        return False  # 거리두기 실패
                    
                    # 다음 위치가 파티션이라면, 이동 불가
                    if room[nx][ny] == "X":
                        continue
                    
                    q.append((nx, ny, dst+1))
        
        return True
    
    for room in places:  # 5개 대기실 확인
        distance_success = True
        
        for r in range(5):
            for c in range(5):
                
                if room[r][c] == "P":  # 응시자라면
                    if not bfs(r, c, 0):  # 거리두기 실패라면
                        distance_success = False 
                        break
        
        if distance_success:  # 거리두기 성공하면
            answer.append(1) 
        else:  # 거리두기 실패라면
            answer.append(0)
            
    return answer