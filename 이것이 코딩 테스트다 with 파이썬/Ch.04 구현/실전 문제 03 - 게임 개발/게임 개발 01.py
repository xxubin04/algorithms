# 이것이 코테다 p.118
# Ch.4 구현 
# 실전 문제 3 - 게임 개발
# 걸린 시간: 1시간 반
# 일시: 2025.02.03
# 코드 잘못된 부분을 GPT에게 조언받음

block_cnt = 1
map_info = []
dir_shift = [(-1, 0), (0, 1), (1, 0), (0, -1)]

row, col = map(int, input().split())
r, c, dir = map(int, input().split())

visited = [[0 for _ in range(col)] for _ in range(row)]
visited[r][c] = 1

for _ in range(row):
  map_info.append(list(map(int, input().split())))

if map_info[r][c] == 1:  # 만약 처음의 위치가 바다라면 
  print(0)
  exit()

while True:
  moved = False  # 이동 여부 확인 
  for i in range(4):
    dir = (dir + 3) % 4  # 왼쪽으로 회전 
    dr, dc = r + dir_shift[dir][0], c + dir_shift[dir][1]  
    if visited[dr][dc] == 0 and map_info[dr][dc] == 0:  # 왼쪽에 방문하지 않았고 이동할 곳이 육지라면
      r, c = dr, dc
      visited[r][c] = 1
      block_cnt += 1
      moved = True
      break

  if not moved:  # 이동할 수 없을 때
    nr, nc = r + dir_shift[(dir + 2) % 4][0], c + dir_shift[(dir + 2) % 4][1]
    if map_info[nr][nc] == 1:  # 뒤쪽이 바다라면
      print(block_cnt)
      exit()
    else:  # 뒤쪽이 육지라면
      r, c = nr, nc
