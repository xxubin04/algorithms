from collections import deque

input = open(0).readline

num = int(input())
house = [list(map(int, (input().strip()))) for _ in range(num)]
visited = [[0 for _ in range(num)] for _ in range(num)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    house[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < num and 0 <= ny < num:
                if house[nx][ny] == 1:
                    house[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1

    return cnt

ans = []
for j in range(num):
    for k in range(num):
        if house[j][k] == 1:
            ans.append(bfs(j, k))

print(len(ans))
for c in sorted(ans): print(c)