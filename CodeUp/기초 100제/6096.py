input = open(0).readline

board = []

for i in range(19):
    board.append(list(map(int, input().split())))

for n in range(num := int(input())):
    x, y = map(int, input().split())

    for r in range(19):
        if board[r][y-1] == 0:
            board[r][y-1] = 1
        else:
            board[r][y-1] = 0
    for c in range(19):
        if board[x-1][c] == 0:
            board[x-1][c] = 1
        else:
            board[x-1][c] = 0

for a in range(19):
    for b in range(19):
        print(board[a][b], end=" ")
    print("")
