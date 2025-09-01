import sys

n, m = map(int, sys.stdin.readline().split())
board = []
visited = [[0 for _ in range(m)] for _ in range(n)]
max_sum = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# ㅏ, ㅜ, ㅓ, ㅗ
frame = [[(0, 0), (1, 0), (2, 0), (1, 1)],
         [(0, 0), (0, 1), (0, 2), (1, 1)],
         [(1, 0), (0, 1), (1, 1), (2, 1)],
         [(0, 1), (1, 0), (1, 1), (1, 2)]]

def dfs(x, y, cnt, cal):
    global max_sum
    if cnt == 4:  # 칸 4개라면
        max_sum = max(max_sum, cal)
        return

    for dir in dirs:
        nx, ny = x + dir[0], y + dir[1]

        # 범위를 벗어나거나 이미 방문했다면
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1:
            continue

        visited[nx][ny] = 1
        dfs(nx, ny, cnt + 1, cal + board[nx][ny])
        visited[nx][ny] = 0

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visited[i][j] = 0

for f in range(4):
    for x in range(n):
        for y in range(m):
            flag = False
            if f == 0:
                if 0 <= x + 2 < n and 0 <= y + 1 < m:
                    flag = True
            elif f == 1:
                if 0 <= x + 1 < n and 0 <= y + 2 < m:
                    flag = True
            elif f == 2:
                if 0 <= x + 2 < n and 0 <= y + 1 < m:
                    flag = True
            else:
                if 0 <= x + 1 < n and 0 <= y + 2 < m:
                    flag = True

            if flag:
                sum = 0
                for i in range(4):
                    fr = frame[f]
                    sum += board[x + fr[i][0]][y + fr[i][1]]
                max_sum = max(max_sum, sum)

print(max_sum)