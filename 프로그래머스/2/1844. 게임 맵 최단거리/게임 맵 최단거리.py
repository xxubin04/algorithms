from collections import deque

dirs = [(0, 1), (1, 0), (-1, 0), (0,-1)]

def bfs(map, n, m):
    q = deque([(0, 0, 1)])
    
    while q:
        x, y, dist = q.popleft()  # x좌표, y좌표, 거리
        
        if x == n-1 and y == m-1:  # 도착했다면 현재 거리 반환
            return dist
        
        for i in range(4):
            nx, ny = x + dirs[i][0], y + dirs[i][1]
            
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 1:
                q.append((nx, ny, dist+1))
                map[nx][ny] = 0
        
    return -1  # 상대 팀 진영에 도착할 수 없는 경우

    
def solution(maps):
    n, m = len(maps), len(maps[0])
    
    return bfs(maps, n, m)