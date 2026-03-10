from collections import deque
input = open(0).readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
q = deque([(0, 0)])

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[N-1][M-1]

print(bfs())