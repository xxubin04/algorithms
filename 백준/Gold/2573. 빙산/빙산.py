from collections import deque
input = open(0).readline

q = deque()
r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt():
    new_graph = [[0]*c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:  # 빙산이면
                cnt = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c:
                        if graph[nx][ny] == 0:
                            cnt += 1
                new_graph[x][y] = max(0, graph[x][y] - cnt)

    return new_graph

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

year = 0
while True:
    visited = [[0] * c for _ in range(r)]
    cnt = 0

    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1

    if cnt >= 2:
        print(year)
        break

    if cnt == 0:
        print(0)
        break

    graph = melt()
    year += 1