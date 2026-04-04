def solution():
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    com = list(map(int, input().split()))

    dice = [0] * 6  # 위0 앞1 오2 아3 뒤4 왼5

    dr = [0, 0, 0, -1, 1]
    dc = [0, 1, -1, 0, 0]

    def roll(d):
        top, front, right, bottom, back, left = dice
        if d == 1:  # 동
            dice[2], dice[3], dice[5], dice[0] = top, right, bottom, left
        elif d == 2:  # 서
            dice[5], dice[0], dice[2], dice[3] = top, right, bottom, left
        elif d == 3:  # 북
            dice[3], dice[1], dice[0], dice[4] = front, top, back, bottom
        elif d == 4:  # 남
            dice[0], dice[4], dice[3], dice[1] = front, top, back, bottom

    for c in com:
        nx, ny = x + dr[c], y + dc[c]

        # 범위 벗어나면 무시
        if not (0 <= nx < N and 0 <= ny < M):
            continue

        x, y = nx, ny
        roll(c)

        if board[x][y] == 0:  # 바닥 값이 0이라면
            board[x][y] = dice[3]
        else:   # 바닥 값이 0이 아니라면
            dice[3] = board[x][y]
            board[x][y] = 0

        print(dice[0])

solution()