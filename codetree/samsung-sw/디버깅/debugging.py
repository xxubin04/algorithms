N, M, H = map(int, input().split())

board = [[0] * (N - 1) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

# 현재 사다리가 본인의 선으로 도착하는지 확인
def check():
    for start in range(N):
        col = start

        for row in range(H):
            # 현재 위치에서 오른쪽으로 연결
            if col < N - 1 and board[row][col]:
                col += 1

            # 왼쪽에서 현재 위치로 연결
            elif col > 0 and board[row][col - 1]:
                col -= 1

        # 시작한 세로선과 다른 곳에 도착
        if col != start:
            return False

    return True


answer = 4


# 가로선을 추가하는 백트래킹
def dfs(start, cnt):
    global answer

    # 이미 구한 정답보다 많이 설치했다면 볼 필요 없음
    if cnt >= answer:
        return

    # 현재 상태로 조건 만족
    if check():
        answer = cnt
        return

    # 최대 3개까지만 추가 가능
    if cnt == 3:
        return

    # 가로선을 놓을 수 있는 위치를
    # 1차원 번호로 생각해서 조합 탐색
    for pos in range(start, H * (N - 1)):

        r = pos // (N - 1)
        c = pos % (N - 1)

        # 이미 가로선 존재
        if board[r][c]:
            continue

        # 왼쪽에 가로선 존재
        if c > 0 and board[r][c - 1]:
            continue

        # 오른쪽에 가로선 존재
        if c < N - 2 and board[r][c + 1]:
            continue

        # 가로선 설치
        board[r][c] = 1

        dfs(pos + 1, cnt + 1)

        # 원상복구
        board[r][c] = 0


dfs(0, 0)

if answer == 4:
    print(-1)
else:
    print(answer)