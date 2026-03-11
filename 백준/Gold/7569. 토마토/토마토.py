from collections import deque
input = open(0).readline

q = deque([])
box = []
M, N, H = map(int, input().split())
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    box.append(layer)

def bfs():
    d = 0
    while q:
        z, x, y, d = q.popleft()
        for i in ((0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            nz, nx, ny = z + i[0], x + i[1], y + i[2]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and visited[nz][nx][ny] == 0 and (b := box[nz][nx][ny]) != -1:
                if b == 0:  # 토마토가 익지 않은 상태라면
                    box[nz][nx][ny] = 1  # 토마토의 상태를 익음으로 변경
                q.append((nz, nx, ny, d+1))
                visited[nz][nx][ny] = 1

    return d

for a in range(H):
    for b in range(N):
        for c in range(M):
            if box[a][b][c] == 1 and not visited[a][b][c]:
                q.append((a, b, c, 0))
                visited[a][b][c] = 1
day = bfs()

for i in range(H):
    for j in range(N):
        if 0 in box[i][j]:
            print(-1)
            exit()

print(0 if day == 1 else day)