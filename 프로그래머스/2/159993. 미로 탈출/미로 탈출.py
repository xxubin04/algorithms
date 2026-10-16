from collections import deque

def solution(maps):
    t = 0
    n = len(maps)
    m = len(maps[0])
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    map_grid = []
    main_loc = {}  # 출발점, 출구, 레버 위치 저장
    
    for i in range(n):
        map_grid.append(l := list(maps[i]))

        for j in range(m):
            if l[j] == 'S':  # 출발점
                main_loc['S'] = (i, j)
            elif l[j] == 'E':  # 출구 
                main_loc['E'] = (i, j)

                
    sx, sy = main_loc['S']
    q = deque([(sx, sy)])

    map_dup = [[-1] * m for _ in range(n)]
    map_dup[sx][sy] = 0
    
    # 레버 먼저 찾기
    find_lever = False
    while q:
        x, y = q.popleft()
        
        if maps[x][y] == 'L':
            t += map_dup[x][y]  # 시간 반환
            find_lever = True 
            break
        
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            
            if not 0 <= nx < n:
                continue 
            
            if not 0 <= ny < m:
                continue
            
            if map_dup[nx][ny] >= 0:  # 이미 방문
                continue 
            
            if maps[nx][ny] == 'X':
                continue 
            
            if maps[nx][ny] in ('O', 'E', 'L', 'S'):
                map_dup[nx][ny] = map_dup[x][y] + 1
                q.append((nx, ny))
    
    if not find_lever:
        return -1
    
    map_dup = [[-1] * m for _ in range(n)]
    map_dup[x][y] = t
    q = deque([(x, y)])
    
    # 출구 찾기
    while q:
        x, y = q.popleft()
        
        if maps[x][y] == 'E':
            return map_dup[x][y]
        
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            
            if not 0 <= nx < n:
                continue 
            
            if not 0 <= ny < m:
                continue
            
            if map_dup[nx][ny] > 0:  # 이미 방문
                continue 
            
            if maps[nx][ny] == 'X':
                continue 
            
            if maps[nx][ny] in ('O', 'E', 'L', 'S'):
                map_dup[nx][ny] = map_dup[x][y] + 1
                q.append((nx, ny))
    
    return -1