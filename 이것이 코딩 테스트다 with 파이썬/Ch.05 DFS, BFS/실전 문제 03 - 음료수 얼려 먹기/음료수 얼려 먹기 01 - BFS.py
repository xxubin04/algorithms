from collections import deque

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def bfs(ice_info, r, c, visited):
  queue = deque([(r, c)])
  visited[r][c] = 1

  while queue:
    r, c = queue.popleft()
    for i in range(4):
      dr = r + nx[i]
      dc = c + ny[i]
      if 0 <= dr < n and 0 <= dc < m and ice_info[dr][dc] == '0' and not visited[dr][dc]:
        visited[dr][dc] = 1
        queue.append((dr, dc))

n, m = map(int, input().split())
ice_info = []  # 얼음 틀 정보 리스트 
visited = [[0] * m for _ in range(n)]  # 방문 처리 리스트 
cnt = 0  # 아이스크림 개수 

for _ in range(n):
  ice_info.append(list(input()))

for j in range(n):
  for k in range(m):
    if ice_info[j][k] == '0' and not visited[j][k]:  # 얼음 틀의 정보가 0이면서 방문하지 않은 경우
      bfs(ice_info, j, k, visited)
      cnt += 1  

print(cnt)
