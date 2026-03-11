from collections import deque
input = open(0).readline

q = deque([])
board = []
height = 0
max_area = 0
for _ in range(n := int(input())):
    board.append(l := list(map(int, input().split())))
    height = max(height, max(l))  # 최대 높이 갱신

def bfs(j, k):
    global cnt
    q.append((j, k))
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > h and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

for h in range(height):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0 and board[j][k] > h:
                cnt += 1
                visited[j][k] = 1
                bfs(j, k)

    max_area = max(max_area, cnt)
print(max_area)