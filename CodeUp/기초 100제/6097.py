input = open(0).readline

r, c = map(int, input().split())
board = [[0 for _ in range(c)] for _ in range(r)]
for i in range(n:=int(input().rstrip())):
    l, d, x, y = map(int, input().split())
    for add in range(l):
        if d == 0: # 가로
            board[x-1][y-1+add] = 1
        else: # 세로
            board[x-1+add][y-1] = 1

for a in range(r):
    for b in range(c):
        print(board[a][b], end=" ")
    print("")
