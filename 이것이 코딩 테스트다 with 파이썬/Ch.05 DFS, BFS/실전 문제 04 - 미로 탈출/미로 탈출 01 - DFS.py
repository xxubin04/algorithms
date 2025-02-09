# 이것이 코테다 p.152
# Ch.5 DFS/BFS
# 실전 문제 4. 미로 탈출 
# 걸린 시간: 10분 33초
# 일시: 2025.02.09

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
cnt = 0  # 각 경로에서 셀 칸의 개수 
answer = 999999999  # 탈출하기 위해 이동해야 할 최소 칸의 개수 
maze = []  # 미로 정보 

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def dfs(maze, r, c, visited, cnt):
  global answer
  visited[r][c] = 1  # 방문 처리 
  cnt += 1  # 칸의 개수 +1
  if r == n-1 and c == m-1:  # 미로의 출구 도착 
    answer = min(cnt, answer)
  for i in range(4):
    nr = r + nx[i]
    nc = c + ny[i]
    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maze[nr][nc] == '1':
      dfs(maze, nr, nc, visited, cnt)

for _ in range(n):
  maze.append(list(input().rstrip()))

dfs(maze, 0, 0, visited, 0)

print(answer)
