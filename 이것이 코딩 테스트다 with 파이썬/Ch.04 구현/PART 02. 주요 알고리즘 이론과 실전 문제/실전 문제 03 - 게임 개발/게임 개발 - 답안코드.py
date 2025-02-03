row, col = map(int, input().split())
visited = [[0] * col for _ in range(row)]
map_info = []

r, c, dir = map(int, input().split())
visited[r][c] = 1

for _ in range(row):
  map_info.append(list(map(int, input().split())))

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 왼쪽으로 회전 함수
def turn_left():
  global dir
  dir -= 1
  if dir == -1:
    dir = 3

# 시뮬레이션 시작
answer = 1
turn_time = 0

while True:
  turn_left()
  nr = r + dr[dir]
  nc = c + dc[dir]

  # 회전한 이후에 정면에 가보지 않은 칸이 존재하는 경우 이동
  if visited[nr][nc] == 0 and map_info[nr][nc] == 0:
    visited[nr][nc] = 1
    r, c = nr, nc
    answer += 1
    turn_time = 0
    continue
  # 회전한 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
    
  # 네 방향 다 갈 수 없는 경우
  if turn_time == 4:
    nr, nc = r - dr[dir], c - dc[dir]
    # 뒤로 이동할 수 있다면 이동하기
    if map_info[nr][nc] == 0:
      r, c = nr, nc
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

print(answer)
    
