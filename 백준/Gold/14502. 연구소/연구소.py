import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board):
    q = deque(virus)

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))

    safe = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                safe += 1
    return safe

answer = 0

for walls in combinations(empty, 3):
    board = [row[:] for row in lab]

    for x, y in walls:
        board[x][y] = 1

    answer = max(answer, bfs(board))

print(answer)