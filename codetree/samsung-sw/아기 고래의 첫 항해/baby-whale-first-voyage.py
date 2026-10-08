from collections import deque 

N, r, c, d = map(int, input().split())  # N: 격자판 길이 / r: 고래 초기 행 / c: 고래 초기 열 / d = 방향 

grid = [list(map(int, input().split())) for _ in range(N)]  # 격자판 (바다0 암초1)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북0 동1 남2 서3

r -= 1  # 0-based
c -= 1

visit_seq = [(r + 1, c + 1)]  # 방문 순서
grid[r][c] = -1  # 초기 위치 방문 처리


# [1. 인접 탐험]
def near_exploration(x, y, d):
    # 1. 현재 방향으로 직진
    nx, ny, nd = straight_current(x, y, d)

    if nx != None:  # 갈 곳이 있다면 
        visit_seq.append((nx+1, ny+1))
        return (nx, ny, nd)
    
    # 2. 좌회전 + 직진
    nx, ny, nd = straight_current(x, y, turn_left(d))

    if nx != None:  # 갈 곳이 있다면 
        visit_seq.append((nx+1, ny+1))
        return (nx, ny, nd)
    
    # 3. 우회전 + 직진
    nx, ny, nd = straight_current(x, y, turn_right(d))

    if nx != None:  # 갈 곳이 있다면 
        visit_seq.append((nx+1, ny+1))
        return (nx, ny, nd)

    # 4. 180도 회전 + 직진
    nx, ny, nd = straight_current(x, y, rotate_180(d))

    if nx != None:  # 갈 곳이 있다면 
        visit_seq.append((nx+1, ny+1))
        return (nx, ny, nd)
    
    return (None, None, None)  # 인접 탐험 불가 


# 1. 현재 방향으로 직진
def straight_current(x, y, d):
    nx, ny = x + dirs[d][0], y + dirs[d][1]

    if not 0 <= nx < N:
        return (None, None, None)
    
    if not 0 <= ny < N:
        return (None, None, None)
    
    if grid[nx][ny] in (1, -1):  # 암초거나 이미 방문했다면 
        return (None, None, None)

    return (nx, ny, d)    


# 2. 좌회전 = 90도 회전 3번
def turn_left(cd):
    return (cd + 3) % 4


# 3. 우회전 = 90도 회전 1번
def turn_right(cd):
    return (cd + 1) % 4


# 4. 180도 회전 = 90도 회전 2번
def rotate_180(cd):
    return (cd + 2) % 4 


# [2. 가장 가까운 바다로 이동]
def move_nearest_sea(x, y, d):

    # 1) 현재 위치에서 가장 가까운 미방문 바다 찾기
    q = deque([(x, y, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1

    min_dst = -1
    candidates = []

    while q:
        cx, cy, dst = q.popleft()

        # 이미 최소거리를 찾았고 그보다 멀어졌다면 종료
        if min_dst != -1 and dst > min_dst:
            break

        # 아직 방문하지 않은 바다 발견
        if grid[cx][cy] == 0:
            if min_dst == -1:
                min_dst = dst

            if dst == min_dst:
                candidates.append((cx, cy))

        # 이미 최소거리 후보를 찾았다면 더 탐색할 필요 없음
        if min_dst != -1:
            continue

        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if visited[nx][ny]:
                continue

            # 암초는 통과 불가능
            if grid[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny, dst + 1))

    # 더 이상 방문할 바다가 없다면
    if not candidates:
        return (None, None, None)

    # 같은 최단거리라면 행 - 열 작은 순
    candidates.sort(key=lambda x: (x[0], x[1]))
    target_x, target_y = candidates[0]


    # 2) target에서 역방향 BFS (각 칸에서 target까지의 거리 계산)
    dist = [[-1] * N for _ in range(N)]

    q = deque([(target_x, target_y)])
    dist[target_x][target_y] = 0

    while q:
        cx, cy = q.popleft()

        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if dist[nx][ny] != -1:  # 이미 방문한 곳이라면
                continue

            # 암초는 이동 불가
            if grid[nx][ny] == 1:
                continue

            dist[nx][ny] = dist[cx][cy] + 1
            q.append((nx, ny))


    # 3) target으로 실제 이동 (0 북 / 1 동 / 2 남 / 3 서)
    move_order = [3, 2, 1, 0]

    while dist[x][y] > 0:

        for nd in move_order:
            dx, dy = dirs[nd]
            nx, ny = x + dx, y + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            # target까지의 거리가 1 감소해야 함
            if dist[nx][ny] != dist[x][y] - 1:
                continue

            # 아직 방문하지 않은 바다라면 방문 순서 기록
            if grid[nx][ny] == 0:
                visit_seq.append((nx + 1, ny + 1))
                grid[nx][ny] = -1

            # 실제 위치와 방향 갱신
            x, y = nx, ny
            d = nd
            break

    return (x, y, d)


# [메인]
# 방향 초기화
if d == 1:
    d = 0
elif d == 2:
    d = 2
elif d == 3:
    d = 3
elif d == 4:
    d = 1

while True:

    if not any(0 in row for row in grid):  # 다 방문했다면 
        break

    # 1. 인접 탐험 
    nx, ny, nd = near_exploration(r, c, d)

    if nx is not None:  # 인접 탐험 가능하면
        grid[nx][ny] = -1  # 방문 처리
        r, c, d = nx, ny, nd

    # 2. 가장 가까운 바다로 이동
    else:  # 인접 탐험 불가능하면 
        r, c, d = move_nearest_sea(r, c, d)

        if r is None:
            break
        
for rc in visit_seq:
    print(*rc)