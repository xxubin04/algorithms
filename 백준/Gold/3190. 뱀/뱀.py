from collections import deque
input = open(0).readline

def solution():
    N = int(input())
    K = int(input())

    board = [[0]*N for _ in range(N)]

    for _ in range(K):
        r, c = map(int, input().split())
        board[r-1][c-1] = 1  # 사과 위치

    com = {}  # 방향 전환 명령 저장
    for _ in range(L := int(input())):
        t, d = input().strip().split()
        com[int(t)] = d

    # 방향: 우=0, 하=1, 좌=2, 상=3
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    snake = deque()
    snake.append((0, 0))  # 시작
    board[0][0] = 2  # 2 = 뱀 몸통

    direction = 0  # 처음엔 오른쪽
    time = 0

    while True:
        time += 1

        head_r, head_c = snake[0]
        next_r = head_r + dr[direction]
        next_c = head_c + dc[direction]

        if not (0 <= next_r < N and 0 <= next_c < N):  # 벽이라면
            break
        if board[next_r][next_c] == 2:  # 몸통이라면
            break

        snake.appendleft((next_r, next_c))  # 머리 좌표 추가

        if board[next_r][next_c] == 1:  # 사과 있음
            board[next_r][next_c] = 2  # 뱀 몸통으로
        else:
            board[next_r][next_c] = 2
            tail_r, tail_c = snake.pop()
            board[tail_r][tail_c] = 0

        if time in com:
            if com[time] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
    print(time)

solution()