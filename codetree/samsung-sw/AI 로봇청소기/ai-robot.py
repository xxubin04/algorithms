import sys 
from collections import deque

input = sys.stdin.readline

N, K, L = map(int, input().rstrip().split())  # N: 격자의 크기 / K: 로봇 청소기의 개수 / L: 테스트 횟수
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우선순위대로 나열 (동0 남1 서2 북3)
dir_comb = [(3, 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, 0)]

# 격자판 정보 저장
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
cleaners = []  # 청소기의 위치 좌표 저장 

# 청소기 위치
for _ in range(K):
    cx, cy = map(int, input().rstrip().split())  # 청소기의 좌표 입력받음
    cx -= 1
    cy -= 1  # 0-based
    cleaners.append((cx, cy))


# 1. 청소기 이동
def move_cleaner(idx, x, y):
    start_x, start_y = x, y
    q = deque([(x, y, 0)])
    visited = [[0] * N for _ in range(N)]  # 방문 여부
    visited[x][y] = 1

    min_dst = -1  # 먼지가 있는 최소 거리
    next_x, next_y = N, N   # 이동할 x, y 좌표

    while q:
        x, y, dst = q.popleft()

        # 이미 최소 거리를 찾았고, 그보다 먼 거리라면 탐색 종료
        if min_dst != -1 and dst > min_dst:
            break 

        # 오염 격자라면
        if grid[x][y] > 0:
            # 첫 오염 격자라면 최소 거리 설정
            if min_dst == -1:
                min_dst = dst 
                next_x, next_y = x, y
            
            # 같은 최소거리라면 행, 열 작은대로 좌표 선택
            elif dst == min_dst:
                if (x, y) < (next_x, next_y):
                    next_x, next_y = x, y 

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy 

            if not 0 <= nx < N:
                continue 
            
            if not 0 <= ny < N:
                continue 
            
            if not visited[nx][ny] == 0:
                continue 
            
            if grid[nx][ny] == -1:
                continue 
            
            if (nx, ny) in cleaners:
                continue 
            
            visited[nx][ny] = 1
            q.append((nx, ny, dst+1))
    
    # 이동 가능한 오염 격자가 없다면 현재 위치 유지
    if min_dst == -1:
        return (start_x, start_y)
    
    return (next_x, next_y)


# 2. 청소 
# 우선순위: 동0 남1 서2 북3
# [0] 북동남(3, 0, 1) / [1] 동남서(0, 1, 2) / [2] 남서북(1, 2, 3) / [3] 서북동(2, 3, 0) 
def clean(i, x, y):
    max_dust = -1  # 청소할 수 있는 먼지의 최대량
    max_dir = 0  # 청소할 방향

    # 현재 청소기의 위치의 먼지 제거
    if (d := grid[x][y]) >= 20:
        grid[x][y] -= 20
    else:
        grid[x][y] = 0
    
    cleaners[idx] = (x, y)

    for dir_idx, comb in enumerate(dir_comb):
        dust_by_dir = 0  # 방향당 먼지 청소량
    
        for j in comb:
            nx, ny = x + dirs[j][0], y + dirs[j][1]

            if not 0 <= nx < N:
                continue 
            
            if not 0 <= ny < N:
                continue 
            
            if grid[nx][ny] == -1:
                continue 
            
            if (d := grid[nx][ny]) >= 20:
                dust_by_dir += 20
            else:
                dust_by_dir += d
        
        if dust_by_dir > max_dust:
            max_dust = dust_by_dir
            max_dir = dir_idx  # 먼지량이 가장 최대일 때의 방향 저장
    
    # 선택한 방향으로 청소
    for j in dir_comb[max_dir]:
        nx, ny = x + dirs[j][0], y + dirs[j][1]

        if not 0 <= nx < N:
            continue 
        
        if not 0 <= ny < N:
            continue 
        
        if grid[nx][ny] == -1:
            continue 

        if (d := grid[nx][ny]) >= 20:
            grid[nx][ny] -= 20
        else:
            grid[nx][ny] = 0
    
    return 
            

# 3. 먼지 축적
def accumulate_dust():
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                grid[i][j] += 5
    return 


# 4. 먼지 확산
def spread_dust():
    grid_dup = [row[:] for row in grid]

    for x in range(N):
        for y in range(N):
            
            # 깨끗한 격자에만 먼지가 확산됨
            if grid[x][y] != 0:
                continue 

            surround_sum = 0   # 주변의 먼지량 합

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if not 0 <= nx < N:
                    continue 
                
                if not 0 <= ny < N:
                    continue 
                
                if grid[nx][ny] > 0:
                    surround_sum += grid[nx][ny]
            
            grid_dup[x][y] = surround_sum // 10 
    
    return grid_dup


# 메인
for _ in range(L):
    # 1. 청소기 이동
    for idx in range(K):
        x, y = cleaners[idx]

        next_x, next_y = move_cleaner(idx, x, y)

        cleaners[idx] = (next_x, next_y)

    # 2. 청소
    for idx in range(K):
        x, y = cleaners[idx]

        clean(idx, x, y)

    # 3. 먼지 축적
    accumulate_dust()

    # 4. 먼지 확산
    grid = spread_dust()

    # 5. 출력
    total = 0

    for x in range(N):
        for y in range(N):
            if grid[x][y] > 0:
                total += grid[x][y]
    
    if total == 0:
        print(0)
        break

    print(total)