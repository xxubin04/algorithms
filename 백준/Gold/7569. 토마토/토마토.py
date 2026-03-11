from collections import deque
input = open(0).readline

q = deque([])
box = []
M, N, H = map(int, input().split())

for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    box.append(layer)

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in ((0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            nz, nx, ny = z + i[0], x + i[1], y + i[2]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1  # 토마토의 상태가 익었거나 익지 않은 경우 -> 일자로 저장
                q.append((nz, nx, ny))

for a in range(H):
    for b in range(N):
        for c in range(M):
            if box[a][b][c] == 1:
                q.append((a, b, c))

bfs()

for i in range(H):
    for j in range(N):
        if 0 in box[i][j]:
            print(-1)
            exit()

print(0 if (day := (max(max(row) for layer in box for row in layer))) == 1 else day-1)
