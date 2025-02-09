# 이것이 코테다 p.149
# Ch.5 DFS/BFS
# 실전 문제 3. 음료수 얼려 먹기 
# 걸린 시간: 23분 57초 
# 일시: 2025.02.09

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def dfs(ice_info, r, c, visited):
  visited[r][c] = 1
  for i in range(4):  # 상하좌우 탐색 
    dr = r + nx[i]
    dc = c + ny[i]
    # 좌표가 얼음 틀 내부에 존재하면서 얼음 틀의 정보가 0이면서 방문하지 않았다면 
    if 0 <= dr < n and 0 <= dc < m and ice_info[dr][dc] == '0' and not visited[dr][dc]:
      dfs(ice_info, dr, dc, visited)
  
n, m = map(int, input().split())  # 행, 열 입력받음 
ice_info = []  # 얼음 틀 정보 리스트 
visited = [[0] * m for _ in range(n)]  # 방문 처리 리스트 
cnt = 0  # 아이스크림 개수 

for _ in range(n):
  ice_info.append(list(input()))

for j in range(n):
  for k in range(m):
    if ice_info[j][k] == '0' and not visited[j][k]:  # 얼음 틀의 정보가 0이면서 방문하지 않은 경우
      dfs(ice_info, j, k, visited)
      cnt += 1  

print(cnt)
