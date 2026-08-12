from collections import deque

k, m = map(int, input().split())

graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))

wall = deque(map(int, input().split()))


# ======== 1) 90도 회전 ========
def rotate_90(i, j, g):
    sx = i - 1
    sy = j - 1

    small = []

    for x in range(sx, sx + 3):
        small.append(g[x][sy:sy + 3])

    rotated = list(map(list, zip(*small[::-1])))
    temp_g = [row[:] for row in g]

    for x in range(5):
        for y in range(5):
            if sx <= x < sx + 3 and sy <= y < sy + 3:
                temp_g[x][y] = rotated[x - sx][y - sy]

    return temp_g


# ======== 2) 연결된 유물 탐색 ========
def dfs(num, x, y):
    visited[x][y] = 1
    nodes.append((x, y))

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if (
            0 <= nx < 5
            and 0 <= ny < 5
            and temp_g[nx][ny] == num
            and visited[nx][ny] == 0
        ):
            dfs(num, nx, ny)

answers = []

# ======== K번 탐사 ========
for _ in range(k):
    max_value = 0
    max_nodes = []
    max_temp_g = []

    best_key = None   # 최적 후보 비교용

    # 9개의 중심 위치
    for i in range(1, 4):
        for j in range(1, 4):

            temp_g = [row[:] for row in graph]

            # 90도, 180도, 270도
            for r in range(3):
                temp_g = rotate_90(i, j, temp_g)

                con_nodes = []
                visited = [[0] * 5 for _ in range(5)]

                # 회전된 전체 5x5에서 유물 탐색
                for x in range(5):
                    for y in range(5):
                        if not visited[x][y]:
                            nodes = []

                            dfs(temp_g[x][y], x, y)

                            if len(nodes) >= 3:
                                con_nodes.extend(nodes)

                value = len(con_nodes)

                # 우선순위
                # 1. 가치 큰 것
                # 2. 회전 각도 작은 것
                # 3. 중심 열 작은 것
                # 4. 중심 행 작은 것
                key = (value, -r, -j, -i)

                if best_key is None or key > best_key:
                    best_key = key
                    max_value = value
                    max_nodes = con_nodes[:]
                    max_temp_g = [row[:] for row in temp_g]

    # 유물을 하나도 획득할 수 없으면 전체 탐사 종료
    if max_value == 0:
        break

    # 선택된 회전을 실제 graph에 적용
    graph = max_temp_g

    # 전체 누적이 아니라 "이번 턴" 점수
    turn_total = 0

    # 최초 획득할 유물
    current_nodes = max_nodes

    # ======== 연쇄 유물 획득 ========
    # while True는 여기에 들어가야 함
    while current_nodes:

        turn_total += len(current_nodes)

        # 벽면 숫자 채우기 순서
        current_nodes = deque(sorted(current_nodes, key=lambda x: (x[1], -x[0])))

        # 유물이 사라진 자리에 벽면 숫자 채우기
        while current_nodes:
            x, y = current_nodes.popleft()
            graph[x][y] = wall.popleft()

        # 새로운 숫자를 채웠으므로 다시 연결된 유물 탐색
        temp_g = graph

        con_nodes = []
        visited = [[0] * 5 for _ in range(5)]

        for x in range(5):
            for y in range(5):
                if not visited[x][y]:
                    nodes = []

                    dfs(temp_g[x][y], x, y)

                    if len(nodes) >= 3:
                        con_nodes.extend(nodes)

        # 다음 연쇄 획득 대상
        current_nodes = con_nodes

    answers.append(turn_total)

print(*answers)