from collections import deque 

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동남서북
n, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
shift = 0  # 계란의 이동 횟수 

def bfs(i, j):
    global L, R, areas, moved

    q = deque([(i, j)])
    visited[i][j] = 1
    areas[-1].append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if L <= abs(board[nx][ny] - board[x][y]) <= R: 
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    areas[-1].append((nx, ny))
    
    if len(areas[-1]) >= 2:
        moved = True  # 합쳐질 영역이 2개 이상 저장됨 -> 합쳐짐 

while True:
    areas = []  # 합칠 영역들 
    visited = [[0] * n for _ in range(n)]  # 방문했는지 여부
    moved = False  # 합칠 영역이 있는지 여부 

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                areas.append([])
                bfs(i, j)
    
    for area in areas:
        total = 0
        for ax, ay in area:
            total += board[ax][ay]
        
        egg = total // len(area)

        for ax, ay in area:
            board[ax][ay] = egg

    if not moved:  # 합칠 영역이 없다면
        break
    
    shift += 1

print(shift)