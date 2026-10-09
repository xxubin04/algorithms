from collections import deque

N, M, K = map(int, input().split())  # N: 격자 크기 / M: 바다거북 수 / K: 해저 화산 수
grid = [list(map(int, input().split())) for _ in range(N)]  # 격자판 좌표 (1: 산호초 / -1: 화석)
answer = [-1] * M

# 바다거북의 위치 리스트  [x좌표, y좌표, 상태]
# 상태 (2  : 이동 중, 살아있음 / 0  : 안식처 도착 / -1 : 화석)
turtles = []
for _ in range(M):
    turtles.append((l := list(map(int, input().split()))) + [2])
    grid[l[0]][l[1]] = 2  # 격자판에 거북이 위치 저장

volcano = [list(map(int, input().split())) for _ in range(K)]  # 해저 화산 리스트 [x좌표, y좌표, 현재 압력]
current_pressure = [0] * K   # 현재의 화산마다의 압력
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# [1단계] 바다거북 이동
def move_turtle(x, y, idx):
    shortest_cell = (-1, -1)  # 다음에 이동할 좌표 저장
    shortest_dst = float('inf')  # 최단경로 길이

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
            dst = bfs(nx, ny)  # 인접한 칸 -> 안식처 로의 최단경로 계산

            if dst == -1:  # 최단경로 길이가 -1이라면, 현재의 위치에서 최단경로가 없다는 뜻
                continue

            if dst < shortest_dst:  # 이번에 계산한 최단경로 길이가 더 짧다면 갱신
                shortest_dst = dst
                shortest_cell = (nx, ny)

    return shortest_cell


# 안식처까지의 최단경로 계산
def bfs(x, y):
    q = deque([(x, y, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1

    while q:
        x, y, dst = q.popleft()

        if x == N - 1 and y == N - 1:  # 안식처 도착했다면
            return dst  # 가장 먼저 안식처에 도착한 경로 = 최단경로

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if grid[nx][ny] in (1, 2, -1):  # 산호초 / 살아있는 바다거북 / 화석이라면 통과 X
                continue

            if visited[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny, dst + 1))

    return -1  # 최단경로 없음 (제자리에 머물기)


# [2단계] 화산 압력 증가
def increase_pressure():
    erupt_list = []  # 분출할 화산 리스트
    for idx, v in enumerate(volcano):
        current_pressure[idx] += 10

        if current_pressure[idx] >= v[2]:  # 분출 임계치보다 크거나 같으면 분출
            erupt_list.append(idx)  # erupt_list에 분출하는 화산 인덱스 저장

    return erupt_list


# [3단계] 화산 분출 및 연쇄 반응
def erupt_chain(erupt_list):
    e = deque(erupt_list)

    while e:
        idx = e.popleft()
        x, y, pressure = volcano[idx]  # 분출하는 화산의 x좌표, y좌표, 현재의 압력
        grid_dup[x][y] += pressure

        for dx, dy in dirs:
            straight_sum(x, y, dx, dy, pressure)

        # 열기 다 더하고 나서 또 분출할 화산이 있다면 큐에 추가
        for idx, vList in enumerate(volcano):
            vx, vy, pressure = vList

            if current_pressure[idx] + grid_dup[vx][vy] >= pressure and not erupted[idx]:  # 아직 분출하지 않은 화산 중 압력이 넘어섰다면 추가
                erupted[idx] = 1
                e.append(idx)


# 해당 방향으로 직진하면서 열기 더하기
def straight_sum(x, y, dx, dy, half):
    nx, ny = x + dx, y + dy
    half //= 2

    if 0 <= nx < N and 0 <= ny < N:
        if grid[nx][ny] == 1 or half == 0:  # 해당 위치가 산호초거나 열기가 0이면 중단
            return

        grid_dup[nx][ny] += half
        straight_sum(nx, ny, dx, dy, half)

    return

def turtle_fossil():
    for idx, (tx, ty, status) in enumerate(turtles):
        if grid_dup[tx][ty] >= 20 and status == 2:  # 살아있는 거북의 위치에 열기가 20 이상이면 화석
            grid[tx][ty] = -1  # 해당 자리에 화석화
            turtles[idx][2] = -1  # 거북이의 상태도 -1로 저장
            answer[idx] = -1



# [4단계] 환경 초기화
def init_env():
    for idx in range(K):
        if erupted[idx] == 1:  # 분출했다면 압력 0으로 변경
            current_pressure[idx] = 0


# 최대 100턴

for turn in range(1, 101):
    # [1단계] 바다거북 이동
    # 1) 현재 거북이의 4방향 -> 안식처 까지의 최단경로이면서 우선순위 만족하는 방향 찾기
    for tidx in range(M):
        x, y, status = (t := turtles[tidx])  # 거북이의 x좌표, y좌표, 상태
        if status != 2:  # 살아있는 거북이 아니라면
            continue

        # 살아있는 거북이라면
        mx, my = move_turtle(x, y, tidx)  # 이동할 좌표

        # 만약 이동할 좌표가 (-1, -1)이라면
        if mx == -1 and my == -1:  # 최단경로 없음 -> 제자리에 머묾
            continue

        # 거북이 위치 갱신
        grid[x][y] = 0
        t[0], t[1] = mx, my

        # 안식처에 도착한 경우
        if mx == N - 1 and my == N - 1:
            t[2] = 0  # 도착 완료 상태
            answer[tidx] = turn
            grid[mx][my] = 0  # 안식처를 차지하지 않도록 비워주기
        # 아직 이동 중인 경우
        else:
            grid[mx][my] = 2

    # [2. 화산 압력 증가]
    erupt_list = increase_pressure()  # 분출할 화산들 인덱스 저장 리스트

    # [3. 화산 분출 및 연쇄 반응]
    if len(erupt_list) == 0:  # 분출할 화산이 없다면 다음 턴으로 넘어갑
        continue

    grid_dup = [[0] * N for _ in range(N)]  # 열기 합산할 격자판 생성

    erupted = [0] * K  # 이미 분출한 화산인지 체크
    for idx in erupt_list:
        erupted[idx] = 1

    erupt_chain(erupt_list)  # 연쇄 분출
    turtle_fossil()  # 화석화

    # [4. 환경 초기화]
    init_env()

print(*answer, sep='\n')