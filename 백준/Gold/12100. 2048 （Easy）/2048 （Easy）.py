input = open(0).readline

# 왼쪽으로 미는 함수
def move_left(board, N):
    new_board = []
    for row in board:
        com_board = [x for x in row if x != 0]  # 0은 제거
        merged = []
        i = 0
        while i < len(com_board):
            if i + 1 < len(com_board) and com_board[i] == com_board[i+1]:
                merged.append(com_board[i] * 2)
                i += 2 # 합친 칸은 건너뛰기
            else:
                merged.append(com_board[i])
                i += 1
        # 뒤를 0으로 채우기 (다음번에 회전하고 다시 계산하기 위해서)
        merged += [0] * (N - len(merged))
        new_board.append(merged)
    return new_board

def rotate(board, N):
    # 보드를 시계방향으로 90도 회전
    return [list(row) for row in zip(*board[::-1])]

def dfs(board, N, depth):
    global ans
    if depth == 5:
        ans = max(ans, max(map(max, board)))
        return

    for _ in range(4):
        moved = move_left(board, N)
        dfs(moved, N, depth + 1)
        board = rotate(board, N)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(board, N, 0)
print(ans)