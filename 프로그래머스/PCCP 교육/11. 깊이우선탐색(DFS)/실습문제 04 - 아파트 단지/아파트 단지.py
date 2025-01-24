def dfs(r, c):
    global cnt
    visited[r][c] = 1
    cnt += 1
    for k in range(4):
        dx = r+nx[k]
        dy = c+ny[k]
        if 0 <= dx < height and 0 <= dy < width and visited[dx][dy] == 0 and arr[dx][dy] == '*':
            dfs(dx, dy)

width, height = map(int, input().split())

cnt = 0
max_cnt = 0

arr = []
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]
visited = [[0 for _ in range(width)] for _ in range(height)]

for _ in range(height):
    arr.append(list(input().strip()))
    
for i in range(height):
    for j in range(width):
        if not visited[i][j] and arr[i][j] == '*':
            cnt = 0
            dfs(i, j)
            max_cnt = max(cnt, max_cnt)
            
print(max_cnt)
