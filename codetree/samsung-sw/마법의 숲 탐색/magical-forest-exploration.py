from collections import deque

R, C, K = map(int, input().split())

# 위쪽에 가상 공간 3칸 추가
H = R + 3

forest = [[0] * C for _ in range(H)]

# 북0 동1 남2 서3
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 골렘의 5칸: 북, 동, 남, 서, 중앙
golem = [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)]

# 모든 골렘의 출구 좌표
exit_cells = set()

# 범위 확인
def is_in_bound(x, y):
    return 0 <= x < H and 0 <= y < C


# 중심이 (x, y)일 때 골렘을 놓을 수 있는지 확인
def can_move(x, y):
    for dx, dy in golem:
        nx, ny = x + dx, y + dy

        if not is_in_bound(nx, ny):
            return False

        if forest[nx][ny] != 0:
            return False

    return True


# 남쪽으로 한 칸 이동 가능한지
def move_south(x, y):
    return can_move(x + 1, y)


# 서쪽으로 굴러 내려갈 수 있는지
def move_west(x, y):
    # 1. 왼쪽 한 칸 이동 가능
    # 2. 거기서 아래 한 칸 이동 가능
    return (can_move(x, y - 1) and can_move(x + 1, y - 1))


# 동쪽으로 굴러 내려갈 수 있는지
def move_east(x, y):
    return (can_move(x, y + 1) and can_move(x + 1, y + 1))


# 골렘을 숲에 기록
def draw_golem(num, x, y, exit_dir):
    for dx, dy in golem:
        nx, ny = x + dx, y + dy
        forest[nx][ny] = num

    # 출구 좌표
    ex = x + dirs[exit_dir][0]
    ey = y + dirs[exit_dir][1]

    exit_cells.add((ex, ey))


# 골렘 내부 및 다른 골렘으로 정령 이동
def move_soul(x, y):
    q = deque([(x, y)])

    visited = [[False] * C for _ in range(H)]
    visited[x][y] = True

    max_row = x

    while q:
        cx, cy = q.popleft()

        max_row = max(max_row, cx)

        current_num = forest[cx][cy]

        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy

            if not is_in_bound(nx, ny):
                continue

            if visited[nx][ny]:
                continue

            # 골렘이 없는 곳으로는 갈 수 없음
            if forest[nx][ny] == 0:
                continue

            next_num = forest[nx][ny]

            # 1. 같은 골렘 내부
            if current_num == next_num:
                visited[nx][ny] = True
                q.append((nx, ny))

            # 2. 현재 위치가 출구라면 다른 골렘으로 이동 가능
            elif (cx, cy) in exit_cells:
                visited[nx][ny] = True
                q.append((nx, ny))

    # 가상 행 3개를 추가했으므로 실제 행 번호로 변환
    return max_row - 2


# 골렘 일부가 실제 숲 바깥에 있는지 확인
def exist_out_of_forest(x):
    # 실제 숲은 index 3부터 시작
    # 위쪽 팔이 x-1이므로 x-1 >= 3이어야 함
    return x <= 3


# 숲 초기화
def eliminate_golem():
    for i in range(H):
        for j in range(C):
            forest[i][j] = 0

    exit_cells.clear()


# 메인
row_total = 0

for num in range(1, K + 1):

    col, exit_dir = map(int, input().split())

    # 골렘 중앙 초기 위치
    x = 1
    y = col - 1

    # 갈 수 있는 곳까지 최대한 하강
    while True:

        # 1. 남쪽
        if move_south(x, y):
            x += 1

        # 2. 서쪽으로 굴러 내려감
        elif move_west(x, y):
            x += 1
            y -= 1

            # 출구도 반시계 방향으로 회전
            exit_dir = (exit_dir + 3) % 4

        # 3. 동쪽으로 굴러 내려감
        elif move_east(x, y):
            x += 1
            y += 1

            # 출구도 시계 방향으로 회전
            exit_dir = (exit_dir + 1) % 4

        # 더 이상 내려갈 수 없음
        else:
            break

    # 골렘 일부가 실제 숲 밖이라면 숲 초기화
    if exist_out_of_forest(x):
        eliminate_golem()
        continue

    # 골렘 배치
    draw_golem(num, x, y, exit_dir)

    # 정령이 갈 수 있는 가장 아래 행
    row_total += move_soul(x, y)


print(row_total)