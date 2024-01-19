from collections import deque

input = open(0).readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    cnt = 0

    while q:
        a, b = q.popleft()
        if visited[a][b] == 0:
            visited[a][b] = 1
            cnt += 1
            for i in range(4):
                nx, ny = a + dx[i], b + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1:
                        q.append((nx, ny))
    return cnt

ans = []
for j in range(n):
    for k in range(m):
        if arr[j][k] == 1 and visited[j][k] == 0:
            ans.append(bfs(arr, j, k))

if len(ans) == 0: 
    print(0); print(0)
else: 
    print(len(ans)); print(max(ans))