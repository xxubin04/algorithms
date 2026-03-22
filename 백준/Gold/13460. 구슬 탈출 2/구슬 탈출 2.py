from collections import deque
input = open(0).readline 

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'
        elif board[i][j] == 'O':
            ox, oy = i, j

def move(x, y, dx, dy):
    # 구슬 하나를 방향으로 끝까지 이동, 구멍 빠지면 탈출
    count = 0
    while board[x + dx][y + dy] != '#':
        x += dx
        y += dy
        count += 1
        if x == ox and y == oy:
            break
    return x, y, count

def bfs():
    visited = set()
    visited.add((rx, ry, bx, by))
    queue = deque()
    queue.append((rx, ry, bx, by, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    while queue:
        crx, cry, cbx, cby, cnt = queue.popleft()

        if cnt >= 10:
            continue

        for dx, dy in directions:
            # 각 구슬 이동
            nrx, nry, rc = move(crx, cry, dx, dy)
            nbx, nby, bc = move(cbx, cby, dx, dy)

            # 파란 구슬이 구멍에 빠지면 실패
            if nbx == ox and nby == oy:
                continue

            # 빨간 구슬이 구멍에 빠지면 성공
            if nrx == ox and nry == oy:
                return cnt + 1

            # 두 구슬이 같은 위치면 더 많이 이동한 구슬을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rc > bc:  # 빨간이 더 이동 -> 빨간을 뒤로
                    nrx -= dx
                    nry -= dy
                else:  # 파란이 더 이동 -> 파란을 뒤로
                    nbx -= dx
                    nby -= dy

            state = (nrx, nry, nbx, nby)
            if state not in visited:
                visited.add(state)
                queue.append((nrx, nry, nbx, nby, cnt + 1))

    return -1

print(bfs())