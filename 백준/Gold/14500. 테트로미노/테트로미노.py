N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0

# DFS로 4칸 탐색
def dfs(r, c, depth, total):
    global ans
    if depth == 4:
        ans = max(ans, total)
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, depth+1, total+board[nr][nc])
            visited[nr][nc] = 0  #  백트래킹

# ㅗ 모양 4가지
T_shapes = [
    [(0,0), (1,0), (2,0), (1,1)],
    [(0,0), (1,0), (2,0), (1,-1)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,0), (0,1), (0,2), (-1,1)]
]

for r in range(N):
    for c in range(M):
        # DFS
        visited[r][c] = 1
        dfs(r, c, 1, board[r][c])
        visited[r][c] = 0

        # ㅗ 모양
        for shape in T_shapes:
            total = 0
            valid = True
            for ddr, ddc in shape:
                nr, nc = r + ddr, c +ddc
                if 0 <= nr < N and 0 <= nc < M:
                    total += board[nr][nc]
                else:
                    valid = False
                    break
            if valid:
                ans = max(ans, total)

print(ans)