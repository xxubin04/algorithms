import sys
input = sys.stdin.readline

N, M = map(int, input().split())
office = []
cctvs = []

for i in range(N):
    row = list(map(int, input().split()))
    office.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctvs.append((row[j], i, j))

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV 종류별 가능한 방향 조합
dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def watch(board, x, y, direction):
    nx, ny = x, y
    while True:
        nx += dx[direction]
        ny += dy[direction]

        if not (0 <= nx < N and 0 <= ny < M):
            break
        if board[nx][ny] == 6:
            break
        if board[nx][ny] == 0:
            board[nx][ny] = '#'

def count_blind(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    return cnt

answer = float('inf')

def dfs(depth, board):
    global answer

    if depth == len(cctvs):
        answer = min(answer, count_blind(board))
        return

    cctv_type, x, y = cctvs[depth]

    for case in dirs[cctv_type]:
        new_board = [row[:] for row in board]

        for d in case:
            watch(new_board, x, y, d)

        dfs(depth + 1, new_board)

dfs(0, office)
print(answer)