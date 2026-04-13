from collections import deque 
import sys 
input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]  # 단지정보 및 방문여부
dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # 동0 남1 서2 뷱3
homes = []  # 단지에 속하는 집 개수들 저장 

def bfs(x, y, num):
    q = deque([(x, y)])
    cnt = 1  # 같은 단지의 집 개수 

    while q:
        rx, ry = q.popleft()
        
        for d in dirs:
            nx, ny = rx + d[0], ry + d[1]
            
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '1':
                cnt += 1
                board[nx][ny] = '2'
                q.append((nx, ny))

    homes.append(cnt)
    return 

for r in range(N):
    for c in range(N):
        if board[r][c] == '1':  # 방문하지 않은 집이라면
            board[r][c] = '2'
            bfs(r, c, board[r][c])
            

print(len(homes))
for h in sorted(homes):
    print(h)