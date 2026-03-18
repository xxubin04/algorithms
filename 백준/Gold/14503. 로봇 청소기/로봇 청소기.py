input = open(0).readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cleaned = 0

while True:
    # 1. 현재 칸 청소
    if graph[x][y] == 0:
        graph[x][y] = -1
        cleaned += 1

    moved = False  # 한 칸 전진했는지의 여부

    # 2. 4방향 탐색
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽 회전
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny
            moved = True
            break

    # 3. 4방향 모두 못 감
    if not moved:
        back = (d + 2) % 4
        nx = x + dx[back]
        ny = y + dy[back]

        # 뒤가 벽이면 종료
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                break
            else:
                x, y = nx, ny

print(cleaned)