from collections import deque

# 필요한 정보 입력
N, M, K = map(int, input().split())  # 격자 크기 N, 바다 거북 수 M, 해저 화산 수 K
graph = [list(map(int, input().split())) for _ in range(N)]  # 격자의 정보 입력 (0: 빈 공간, 1: 산호초, 2: 바다거북, 3: 화석)
turtle_loc = [tuple(map(int, input().split())) for _ in range(M)]  # 거북이의 위치 정보 입력 (0-based)
volcano_loc = [(list(map(int, input().split())) + [0]) for _ in range(K)]  # 화산의 위치 정보 입력 (0-based) + 화산 압력 0으로 초기화

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
arrive_turn = [-1] * M  # 안식처 도착 턴 저장 (각 idx = 거북이의 id)
turtle_path = []  # 거북이들의 최단 경로 저장
remain_turtle = M  # 아직 안 들어온 거북이 수
for i, j in turtle_loc:  # 좌표에 거북이 위치 표시
    graph[i][j] = 2


## 1단계: 바다거북 이동
# 1-1. 최단경로 탐색
def shortest_path(i, j):
    q = deque([(i, j, [])])  # [(i, j) ~ 안식처]의 최단경로 구함
    visited = [[False] * N for _ in range(N)]  # 방문여부

    while q:
        x, y, path = q.popleft()  # x좌표, y좌표, 지금까지의 경로
        visited[x][y] = True   # 방문처리

        if x == N-1 and y == N-1:  # 안식처에 도착했다면 (가장 처음 도착한 경로가 우선순위에 맞는 경로임)
            return path  # 경로 반환

        for dx, dy in dirs:  # 우하좌상 순서대로 탐색
            nx, ny = x + dx, y + dy

            # 해당 좌표가 격자 범위 안이면서, 이동 가능한지 확인하고, 아직 방문하지 않은 경우
            # 이동 가능 -> 빈 칸(0) / 해저 화산
            if 0 <= nx < N and 0 <= ny < N and check_movable(nx, ny) and not visited[nx][ny]:
                q.append((nx, ny, path + [(nx, ny)]))  # 방문해야 할 위치 및 경로 추가
                # print(f"{nx}, {ny}, {path}")

    return None  # 최단경로가 없다면 None 반환


# 1-2. 이동 가능한지 확인 (빈 칸 or 해저화산)
def check_movable(i, j):
    # 빈 칸인 경우
    if graph[i][j] == 0:
        return True

    # 해저화산인 경우
    for vx, vy, p, press in volcano_loc:
        if (i == vx and j == vy) and not graph[vx][vy] in [2, 3]:
            return True

    return False  # 둘 다 아닌 경우에는 이동 불가


# 1-3. 최단경로대로 1칸 이동
def move_one_block(i, j, id, turn, path):  # 현재 좌표(i, j), 거북이 id, 현재 턴, 최단경로
    global turtle_loc, arrive_turn, graph

    ni, nj = path.pop(0)

    if arrive_safe_place(ni, nj):  # 만약 안식처에 도착하면
        arrive_turn[id] = turn  # 현재의 턴으로 갱신하여 도착 정보 저장
    else:  # 다음 위치가 안식처가 아니라면
        graph[ni][nj] = 2  # 다음 위치로 거북이 위치 갱신

    graph[i][j] = 0  # 현재의 거북이 위치를 빈 칸으로 갱신
    turtle_loc[id] = (ni, nj)  # 거북이의 위치 갱신


# 1-4. 안식처 도착
def arrive_safe_place(i, j):
    global remain_turtle

    if i == N-1 and j == N-1:
        remain_turtle -= 1
        return True

    return False


## 2단계: 화산 압력 증가
# 2-1. 모든 화산의 압력 10씩 증가
def increase_pressure():
    global volcano_loc

    for idx in range(K):  # volcano_loc[idx] = [x좌표, y좌표, 분출 임계치, 현재 압력]
        volcano_loc[idx][3] += 10


## 3단계: 화산 분출 및 연쇄 반응
# 3-1. 열기 분출
def emit_heat(idx, x, y, p, press):
    global temp_graph, emited

    if press < p or emited[idx]:  # 분출 임계치(p)보다 현재 압력(press)가 작거나 이미 분출했다면, 열기 분출X
        return

    emited[idx] = True  # 분출 처리
    heat = p  # 분출 임계치(p)만큼의 열기 발생
    temp_graph[x][y] += heat  # 화산 위치에 열기 더함

    spread_heat(x, y, heat)  # 열기 전파

    # for idx in range(K):
    #     if emited[idx]:  # 이미 분출한 화산이라면 연쇄 반응 X
    #         continue
    #
    #     vx, vy, heat = volcano_loc[idx][0], volcano_loc[idx][1], volcano_loc[idx][2]  # 화산의 x좌표, y좌표, 분출 임계치
    #     emited[idx] = True  # 분출 처리
    #     spread_heat(vx, vy, heat)


# 3-2. 열기가 4방향으로 전파 + 절반씩 줄어듦
def spread_heat(x, y, heat):
    global temp_graph

    # print(f"x: {x}, y: {y}, heat: {heat}")
    for dx, dy in dirs:
        h = heat // 2
        for n in range(1, N):
            nx, ny = x + (dx * n), y + (dy * n)

            # 현재 칸의 좌표가 격자 범위 안이면서, 산호초가 아니라면
            if 0 <= nx < N and 0 <= ny < N and h > 0:
                if graph[nx][ny] == 1:  # 산호초라면, 해당 방향 그만 전파
                    break

                temp_graph[nx][ny] += h  # 열기 저장(전파 O)

            h //= 2  # 이전 칸 열기의 절반만큼 전파

    chain_reaction()  # 연쇄반응이 일어나는지 확인


# 3-3. 연쇄 반응
def chain_reaction():
    global emited

    for idx in range(K):
        if emited[idx]:  # 이미 분출한 화산이라면 연쇄 반응 X
            continue

        vx, vy, p, press = volcano_loc[idx][0], volcano_loc[idx][1], volcano_loc[idx][2], volcano_loc[idx][3]  # 화산의 x좌표, y좌표, 분출 임계치

        if (press + temp_graph[vx][vy]) >= p:
            emited[idx] = True  # 분출 처리
            temp_graph[vx][vy] += p
            spread_heat(vx, vy, p)

    return


# 3-5. 모든 분출 종료 후, 거북 화석화 + 위치 고정
def turtle_fossil():
    global graph, remain_turtle

    for idx in range(M):
        tx, ty = turtle_loc[idx][0], turtle_loc[idx][1]

        # 거북이 화석이 아님 + 열기가 20 이상 + 안식처에 도착한 거북이가 아닌 경우
        if graph[tx][ty] != 3 and temp_graph[tx][ty] >= 20 and arrive_turn[idx] == -1:
            graph[tx][ty] = 3  # 거북이 화석
            remain_turtle -= 1


## 4단계: 환경 초기화
# 4-1. 모든 열기 정보 없어짐(main함수) + 분출 화산의 압력 초기화
def initialize_press():
    global volcano_loc
    for idx in range(K):
        if emited[idx]:  # 이번 턴에 분출한 화산은 압력 0으로 초기화
            volcano_loc[idx][3] = 0


## main
# 턴 최대 100번
turn = 1
while turn <= 100:
    if not remain_turtle:  # 전부 도착했다면 (화석 제외)
        break

    # 1턴 (4단계)
    for id in range(M):
        if arrive_turn[id] != -1:  # 이미 도착한 거북이라면
            continue

        tx, ty = turtle_loc[id]  # 거북이의 현재 위치 좌표
        s_path = shortest_path(tx, ty)  # 매 턴 & 거북이마다 최단 경로 갱신

        if graph[tx][ty] == 3:  # 화석 거북이라면
            continue

        if s_path is None:  # 안식처에 도착할 최단경로가 없다면
            continue

        move_one_block(tx, ty, id, turn, s_path)  # 1칸 이동

    increase_pressure()  # 화산 압력 증가

    temp_graph = [[0] * N for _ in range(N)]  # graph 얕은 복사 (열기 저장 위해)
    emited = [0] * K   # 화산이 분출했는지 여부 저장 (0: 분출X, 1: 분출O)

    # 열기 분출되는 화산은 분출
    for idx in range(K):
        emit_heat(idx, volcano_loc[idx][0], volcano_loc[idx][1], volcano_loc[idx][2], volcano_loc[idx][3])

    turtle_fossil()
    initialize_press()

    turn += 1  # 턴 횟수 1 증가

for at in arrive_turn:
    print(at)

