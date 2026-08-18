from collections import deque

N, cr, cc, cd = map(int, input().split())  # 격자의 칸 수, 현재 행, 현재 열, 현재 방향
remain_sea = 0  # 방문하지 않은 바다 수
sea_loc = []  # 바다의 좌표
dirs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 1: 상, 2: 하, 3: 좌, 4: 우
# [직진, 좌회전, 우회전, 180도]
rotate_dir = [[], [1, 3, 4, 2], [2, 4, 3, 1], [3, 2, 1, 4], [4, 1, 2, 3]]  # 1: 상, 2: 하, 3: 좌, 4: 우
graph = [[2] * (N+1)]  # 격자 (바다: 0, 암호: 1, 방문한 바다: 2)
visit_route = []  # 방문 순서 저장

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    graph.append([2] + row)

    for j in range(1, N + 1):
        if row[j - 1] == 0:
            sea_loc.append((i, j))
            remain_sea += 1


# 1. 방문하지 않은 인접 바다가 존재하는지 확인
# 발견하면 바로 반환 (우선순위에 따라서 확인하므로)
def check_to_visit(r, c):
    global cd

    for nd in rotate_dir[cd]:
        dr, dc = dirs[nd]
        nr, nc = r + dr, c + dc

        # 격자 안에 위치하면서, 인접 칸이 방문하지 않은 바다라면
        if 1 <= nr <= N and 1 <= nc <= N and graph[nr][nc] == 0:
            cd = nd  # 이동 방향 갱신
            return nr, nc  # 인접 칸의 행, 열

    return None  # 방문할 인접한 바다가 없다면 None 반환


# 2. 방문하지 않은 인접 바다로 1칸 이동
def move_near_sea(r, c):
    global cr, cc, remain_sea
    cr, cc = r, c  # 현재 위치 갱신

    graph[cr][cc] = 2
    remain_sea -= 1

    visit_route.append((cr, cc))


# 3. 거리 계산해서 가장 가까운 거리인 칸의 좌표 반환
def cal_dist():
    bfs_near()


# 3-1. 현재 위치에서 바다까지의 최소 거리 찾기
def bfs_near():
    global dist_to_sea

    q = deque([(cr, cc, 0)])

    visited = [[False] * (N + 1) for _ in range(N + 1)]
    visited[cr][cc] = True

    min_dist = -1 # 현재 위치로부터의 최소 거리

    while q:
        r, c, dist = q.popleft()

        # 이미 최소 거리보다 멀어졌다면 종료
        if min_dist != -1 and dist > min_dist:
            break

        # 아직 방문하지 않은 바다 발견
        if graph[r][c] == 0:
            if min_dist == -1:
                min_dist = dist

            dist_to_sea.append((r, c))
            continue

        # 상하좌우 BFS
        for nd in range(1, 5):
            dr, dc = dirs[nd]

            nr, nc = r + dr, c + dc

            if not (1 <= nr <= N and 1 <= nc <= N):
                continue

            # 암초는 지나갈 수 없음
            if graph[nr][nc] == 1:
                continue

            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            q.append((nr, nc, dist + 1))


# 4. 거리가 같은 칸이 여러개면, 행-열 작은 것 반환
def choose_block():
    global dist_to_sea
    # dist_to_sea = sorted(dist_to_sea, key=lambda x: (x[0], x[1]))
    dist_to_sea.sort(key=lambda x: (x[0], x[1]))
    return dist_to_sea[0]


# 5. 거리가 1 줄어드는 칸으로 이동 (우선순위에 맞게)
def bfs_far():
    global cr, cc, cd

    # 목적지까지의 거리 계산
    dist = [[-1] * (N + 1) for _ in range(N + 1)]

    q = deque([(dest_r, dest_c)])
    dist[dest_r][dest_c] = 0

    while q:
        r, c = q.popleft()

        for nd in range(1, 5):
            dr, dc = dirs[nd]

            nr = r + dr
            nc = c + dc

            if not (1 <= nr <= N and 1 <= nc <= N):
                continue

            # 암초는 이동 불가능
            if graph[nr][nc] == 1:
                continue

            if dist[nr][nc] != -1:
                continue

            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

    # 실제 이동 (좌, 하, 우, 상)
    move_priority = [3, 2, 4, 1]
    
    while cr != dest_r or cc != dest_c:
        
        for nd in move_priority:
            dr, dc = dirs[nd]
            
            nr, nc = cr + dr, cc + dc
            
            if not (1 <= nr <= N and 1 <= nc <= N):
                continue
            
            if graph[nr][nc] == 1:
                continue 
            
            # 목적지까지 거리가 1 감소했다면 이동
            if dist[nr][nc] == dist[cr][cc] - 1:
                cr, cc = nr, nc
                cd = nd
                break
    
    # 목적지에 도착했으므로 새로운 바다 방문 처리 
    move_near_sea(cr, cc)

graph[cr][cc] = 2
remain_sea -= 1

visit_route.append((cr, cc))

## 시뮬레이션
# 방문할 바다가 남은 동안
while remain_sea:
    ## 1단계: 인접 탐험
    nt = check_to_visit(cr, cc) 
    
    if nt is not None:
        nr, nc = nt
        move_near_sea(nr, nc) 
        continue
        
    ## 2단계: 가장 가까운 바다로 이동
    dist_to_sea = []  # 현재 위치에서 바다로의 거리가 최소인 좌표들
    cal_dist()
    
    # 더 이상 갈 수 있는 바다가 없다면
    if not dist_to_sea:
        break 
    
    if len(dist_to_sea) == 1:
        dest_r, dest_c = dist_to_sea[0]
    else:
        dest_r, dest_c = choose_block()
    
    # 선택한 바다까지 이동
    bfs_far()

for i, j in visit_route:
    print(i, j)