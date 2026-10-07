from collections import deque

n = int(input())
grid = []
robot_lv = 2  # 로봇의 레벨
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for i in range(n):
    grid.append(l := list(map(int, input().split())))

    if 9 in l:
        x, y = i, l.index(9)


def bfs(x, y):
    q = deque([(x, y, 0)])
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1 
    can_kill = []
    min_dst = 0

    while q:
        x, y, dst = q.popleft()

        if 0 < grid[x][y] < robot_lv:
            if min_dst == 0:
                min_dst = dst  # 0이라면 최소거리로 갱신
                can_kill.append((x, y))
            elif dst == min_dst:
                can_kill.append((x, y))

        if min_dst != 0 and dst > min_dst:
            continue 

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not 0 <= nx < n:
                continue 
            
            if not 0 <= ny < n:
                continue 

            if not visited[nx][ny] == 0:
                continue 
            
            if grid[nx][ny] > robot_lv:
                continue 
            
            visited[nx][ny] = 1
            q.append((nx, ny, dst+1))
    
    if len(can_kill) == 0:
        return None
    
    can_kill.sort(key=lambda x: (x[0], x[1]))

    return (can_kill[0], min_dst)

kill_cnt = 0
t = 0
grid[x][y] = 0

while True:
    if (b := bfs(x, y)) is None:
        break
    else:
        cell, dst = b

    x, y = cell
    grid[x][y] = 0
    t += dst 
    kill_cnt += 1

    if kill_cnt == robot_lv:
        robot_lv += 1
        kill_cnt = 0

print(t)