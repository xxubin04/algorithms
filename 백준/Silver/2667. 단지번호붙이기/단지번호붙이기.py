from collections import deque
input = open(0).readline

N = int(input())
maze = [list(map(int, input().strip())) for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cnt = 0
house_cnt = []

def bfs(dx, dy):
    house = 0
    q = deque([(dx, dy)])
    maze[dx][dy] = -1

    while q:
        x, y = q.popleft()
        house += 1
        for i in range(4):
            nx, ny = x + dirs[i][0], y + dirs[i][1]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 1:
                q.append((nx, ny))
                maze[nx][ny] = -1  # 방문처리

    house_cnt.append(house)

for i in range(N):
    for j in range(N):
        if maze[i][j] == 1:
            cnt += 1
            bfs(i, j)

print(cnt)
print(*sorted(house_cnt), sep='\n')