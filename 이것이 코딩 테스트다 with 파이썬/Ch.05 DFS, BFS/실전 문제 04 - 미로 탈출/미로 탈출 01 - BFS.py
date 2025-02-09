# 이것이 코테다 p.152
# Ch.5 DFS/BFS
# 실전 문제 4. 미로 탈출 
# 일시: 2025.02.09
from collections import deque

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
cnt = 0  # 각 경로에서 셀 칸의 개수 
maze = []  # 미로 정보 

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def bfs(r, c):
  queue = deque()
  queue.append((r, c))
  while queue:
    r, c = queue.popleft()
    for i in range(4):
      nr = r + nx[i]
      nc = c + ny[i]
      if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == '1':
        queue.append((nr, nc))
        maze[nr][nc] = int(maze[r][c]) + 1  # 직전에 방문했던 칸의 순서 + 1
    
  return maze[n-1][m-1]

for _ in range(n):
  maze.append(list(input().rstrip()))

print(bfs(0, 0))
