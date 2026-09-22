from collections import deque

N, K, L = map(int, input().split())  # 격자의 크기 N, 청소기의 개수 K, 테스트 횟수 L
grid = []  # 격자
cleaner = []  # 청소기
dirs1 = [(-1, 0), (0, -1), (0, 1), (1, 0)]
dirs2 = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# 격자 입력
for _ in range(N):
    grid.append(list(map(int, input().split())))

# 청소기 초기 위치 입력
for _ in range(K):
    cx, cy = map(int, input().split())
    cleaner.append((cx-1, cy-1))


# 1. 청소기 이동
def move_cleaner(x, y):
    fx, fy = x, y  # 초기 좌표

    # 현재 위치에 먼지가 있으면 이동하지 않음
    if grid[x][y] > 0:
        return (x, y)

    q = deque([(x, y)])
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1

    while q:
        candidates = []  # 현재 거리에서 발견한 먼지 칸들

        for _ in range(len(q)):
            x, y = q.popleft()

            for dx, dy in dirs1:
                nx, ny = x + dx, y + dy

                # 범위 밖
                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                # 이미 방문
                if visited[nx][ny]:
                    continue

                # 물건이 있는 칸
                if grid[nx][ny] == -1:
                    continue

                # 다른 청소기가 있는 칸
                if occupied[nx][ny]:
                    continue

                visited[nx][ny] = 1

                # 먼지가 있는 칸 발견
                if grid[nx][ny] > 0:
                    candidates.append((nx, ny))
                else:
                    # 깨끗한 칸이면 계속 이동 
                    q.append((nx, ny))

        # 같은 최단거리의 먼지를 모두 확인한 뒤
        if candidates:
            return min(candidates)
                    
    return (fx, fy)  # 이동할 수 없다면 제자리


# 2. 청소
def clean(x, y):
    max_dust = 0  # 최대 먼지량
    total = min(20, grid[x][y])  # 5개의 격자 합 
    num_4 = []  # 4방향의 격자 값 저장 
    mx, my = 0, 0  # 뺼 격자 저장

    # 5개의 격자 합 구하기
    for dx, dy in dirs2:
        nx, ny = x + dx, y + dy
        
        # 범위 안인 경우
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != -1:
            num_4.append((nx, ny))
            total += min(20, grid[nx][ny])
        else:  # 범위 밖인 경우
            num_4.append((-1, -1))
    
    # 1개의 격자씩 값 뺴기
    for i in range(4):
        if num_4[i] == (-1, -1) and max_dust < total:  # 범위 밖인 격자를 빼야한다면, 최댓값 갱신만
            max_dust = total
            mx, my = -1, -1
            continue
        
        n = num_4[i]
        if (t := total - min(20, grid[n[0]][n[1]])) > max_dust:
            max_dust = t  # 최댓값 갱신
            mx, my = n  # 뺄 좌표 저장
    
    # 격자마다 20씩 청소
    if grid[x][y] - 20 <= 0:
        grid[x][y] = 0
    else:
        grid[x][y] -= 20

    for i in range(4):
        nx, ny = num_4[i]
        if (nx, ny) == (mx, my) or (nx, ny) == (-1, -1):  # 빼는 격자거나 범위 밖이라면
            continue 
        
        if grid[nx][ny] - 20 <= 0:
            grid[nx][ny] = 0
        else:
            grid[nx][ny] -= 20


# 3. 먼지 축적
def accumulate_dust():
    for i in range(N):
        for j in range(N):
            if grid[i][j] not in [0, -1]:
                grid[i][j] += 5   # 먼지가 있는 모든 격좌에 5씩 추가 


# 4. 먼지 확산
def spread_dust():
    grid_dup = [row[:] for row in grid]  # 격자 얕은 복사 

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:  # 깨끗한 격자라면
                total = 0  # 주변 4방향의 먼지 합 
                
                for dx, dy in dirs2:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < N and 0 <= ny < N and not grid[nx][ny] == -1:
                        total += grid[nx][ny]
                
                grid_dup[i][j] = total // 10
    
    return grid_dup


# 5. 출력
def print_dust():
    total = 0

    for i in range(N):
        for j in range(N):
            if grid[i][j] == -1:
                continue 
            
            total += grid[i][j]
    
    print(total)


while L:  # 테스트 L번 반복
    L -= 1

    # 청소기 위치 별도 저장 (2차원 배열로)
    occupied = [[False] * N for _ in range(N)]

    for x, y in cleaner:
        occupied[x][y] = True 
    
    for i in range(K):
        x, y = cleaner[i]

        # 기존 위치에서 청소기 제거
        occupied[x][y] = False

        nx, ny = move_cleaner(x, y)

        cleaner[i] = (nx, ny)
        
        # 새로운 위치에 청소기 배치
        occupied[nx][ny] = True
        
    for clx, cly in cleaner:
        # 2. 청소 
        clean(clx, cly)

    # 3. 먼지 축적
    accumulate_dust()

    # 4. 먼지 확산
    grid = spread_dust()

    # 5. 출력
    print_dust()
