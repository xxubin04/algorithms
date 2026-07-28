n, m, t = map(int, input().split())

graph = []
storm = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

    for j in range(m):
        if row[j] == -1:
            storm.append((i, j))

upper = storm[0][0]   # 위쪽 돌풍 행
lower = storm[1][0]   # 아래쪽 돌풍 행

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


# 1. 먼지 확산
def spread():
    next_graph = [[0] * m for _ in range(n)]

    # 돌풍 위치 유지
    next_graph[upper][0] = -1
    next_graph[lower][0] = -1

    for x in range(n):
        for y in range(m):
            # 돌풍 또는 먼지가 없는 칸
            if graph[x][y] <= 0:
                continue

            amount = graph[x][y] // 5

            # 확산할 먼지가 없는 경우
            if amount == 0:
                next_graph[x][y] += graph[x][y]
                continue

            count = 0

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                if graph[nx][ny] == -1:
                    continue

                next_graph[nx][ny] += amount
                count += 1

            # 현재 칸에 남은 먼지
            next_graph[x][y] += graph[x][y] - amount * count

    return next_graph


# 2-1. 위쪽 돌풍: 반시계 방향
def counterclockwise():
    x = upper

    # 왼쪽 열: 위에서 아래
    for i in range(x - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]

    # 맨 위 행: 오른쪽에서 왼쪽
    for j in range(m - 1):
        graph[0][j] = graph[0][j + 1]

    # 오른쪽 열: 아래에서 위
    for i in range(x):
        graph[i][m - 1] = graph[i + 1][m - 1]

    # 돌풍 행: 왼쪽에서 오른쪽
    for j in range(m - 1, 1, -1):
        graph[x][j] = graph[x][j - 1]

    # 돌풍에서 깨끗한 공기가 나옴
    graph[x][1] = 0
    graph[x][0] = -1


# 2-2. 아래쪽 돌풍: 시계 방향
def clockwise():
    x = lower

    # 왼쪽 열: 아래에서 위
    for i in range(x + 1, n - 1):
        graph[i][0] = graph[i + 1][0]

    # 맨 아래 행: 오른쪽에서 왼쪽
    for j in range(m - 1):
        graph[n - 1][j] = graph[n - 1][j + 1]

    # 오른쪽 열: 위에서 아래
    for i in range(n - 1, x, -1):
        graph[i][m - 1] = graph[i - 1][m - 1]

    # 돌풍 행: 왼쪽에서 오른쪽
    for j in range(m - 1, 1, -1):
        graph[x][j] = graph[x][j - 1]

    # 돌풍에서 깨끗한 공기가 나옴
    graph[x][1] = 0
    graph[x][0] = -1


for _ in range(t):
    graph = spread()
    counterclockwise()
    clockwise()

# 돌풍 값 -1 두 개를 제외한 먼지 합
answer = sum(
    graph[i][j]
    for i in range(n)
    for j in range(m)
    if graph[i][j] > 0
)

print(answer)