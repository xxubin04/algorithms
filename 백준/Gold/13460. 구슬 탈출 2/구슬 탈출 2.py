from collections import deque
input = open(0).readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

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

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
def move(x, y, dx, dy):
    count = 0  # 빨간 구슬이랑 파란 구슬 겹쳤을 때 더 많이 움직인 구슬을 옮기기 위해 이동한 칸 개수 저장하는 변수
    while board[x + dx][y + dy] != '#':  # 벽/구멍이 아닐때까지
        count += 1
        x += dx
        y += dy
        if x == ox and y == oy:  # 구멍에 빠진다면
            break
    return x, y, count  # 구슬의 최종 좌표와 이동횟수 반환

def bfs():
    visited = set()
    visited.add((rx, ry, bx, by))
    queue = deque([(rx, ry, bx, by, 0)])

    while queue:
        crx, cry, cbx, cby, cnt = queue.popleft()

        if cnt >= 10:
            continue

        for dx, dy in directions:
            nrx, nry, rc = move(crx, cry, dx, dy)
            nbx, nby, bc = move(cbx, cby, dx, dy)

            # 파란 구슬이 구멍에 빠지면 실패
            if nbx == ox and nby == oy:
                continue  # queue에 있는 다른 경우들도 마저 확인해야 함

            # 빨간 구슬이 구멍에 빠지면 성공
            if nrx == ox and nry == oy:
                return cnt + 1

            # 두 구슬이 같은 위치라면 더 많이 움직인 구슬이 한 칸 뒤로 감
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (state := (nrx, nry, nbx, nby)) not in visited:
                visited.add(state)
                queue.append((nrx, nry, nbx, nby, cnt + 1))

    return -1

print(bfs())