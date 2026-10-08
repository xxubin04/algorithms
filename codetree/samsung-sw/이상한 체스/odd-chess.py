n, m = map(int, input().split())
grid = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 동0 서1 남2 북3
chess_loc = []  # 말이 있는 좌표 저장

for i in range(n):
    l = list(map(int, input().split()))
    grid.append(l)

    for j in range(m):
        # 1 ~ 5번 체스말만 저장
        if 1 <= l[j] <= 5:
            chess_loc.append((i, j))

# 각 체스말마다 갈 수 있는 방향의 조합 (1-based)
# 1번: 동0 서1 남2 북3
# 2번: (동, 서)0 (남, 북)1
# 3번: (동, 북)0 (동, 남)1 (남, 서)2 (서, 북)3
# 4번: (동, 북, 서)0 (북, 동, 남)1 (동, 남, 서)2 (남, 서, 북)3
# 5번: 동남북서0
go_dirs = [
        [],
        [((0, 1),), ((0, -1),), ((1, 0),), ((-1, 0),)],
        [((0, 1), (0, -1)), ((1, 0), (-1, 0))],
        [((0, 1), (-1, 0)), ((0, 1), (1, 0)), ((1, 0), (0, -1)), ((0, -1), (-1, 0))],
        [((0, 1), (-1, 0), (0, -1)), ((-1, 0), (0, 1), (1, 0)), ((0, 1), (1, 0), (0, -1)), ((1, 0), (0, -1), (-1, 0))],
        [((0, 1), (1, 0), (-1, 0), (0, -1))] 
]

def go_straight(temp, x, y, dx, dy):
    nx, ny = x + dx, y + dy

    while 0 <= nx < n and 0 <= ny < m:
        # 벽이면 더 이상 갈 수 없음
        if temp[nx][ny] == 6:
            break

        # 빈칸이라면 감시 영역으로 표시
        if temp[nx][ny] == 0:
            temp[nx][ny] = -1

        # 체스말은 통과 가능
        nx += dx
        ny += dy 

answer = n * m  

# 각 체스말의 방향을 선택
def dfs(idx, temp):
    global answer

    # 모든 체스말의 방향을 정했다면
    if idx == len(chess_loc):
        blind = 0

        # 사각지대 개수 계산
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    blind += 1

        answer = min(answer, blind)
        return


    cx, cy = chess_loc[idx]
    num = grid[cx][cy]

    # 현재 체스말이 가질 수 있는 모든 방향 조합 확인
    for directions in go_dirs[num]:

        # 현재 상태 복사
        next_grid = [row[:] for row in temp]

        # 선택한 방향들로 감시
        for dx, dy in directions:
            go_straight(next_grid, cx, cy, dx, dy)

        # 다음 체스말
        dfs(idx + 1, next_grid)


dfs(0, grid)

print(answer)