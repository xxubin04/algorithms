input = open(0).readline

board = [[0 for _ in range(19)] for _ in range(19)]

for i in range(int(input())):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

for c in range(19):
    for d in range(19):
        print(board[c][d], end=" ")
    print("")
