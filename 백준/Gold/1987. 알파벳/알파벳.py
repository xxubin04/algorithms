import sys

max_cnt = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = set()

def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            alpha = board[nx][ny]
            if alpha not in visited:
                visited.add(alpha)
                dfs(nx, ny, cnt + 1)
                visited.remove(alpha)

visited.add(board[0][0])
dfs(0, 0, 1)
print(max_cnt)