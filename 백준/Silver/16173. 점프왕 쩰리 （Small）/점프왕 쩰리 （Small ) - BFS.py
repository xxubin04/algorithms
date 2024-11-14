# BFS
from collections import deque
input = open(0).readline

n = int(input())
area = []
q = deque()

dx, dy = [0, 1], [1, 0]
visited = [[0 for _ in range(n)] for _ in range(n)]  # 방문처리

def BFS(visited):
    while q:
        x, y = q.popleft()

        for i in range(2):
            nx, ny = x + area[x][y] * dx[i], y + area[x][y] * dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] == -1:
                    return "HaruHaru"

                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
            else:
                continue
    return "Hing"

for i in range(n):
    area.append(list(map(int, input().split())))

q.append((0, 0))
print(BFS(visited))

