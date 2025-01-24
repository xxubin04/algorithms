def dfs(r, c, prior):
    visited[r][c] = 1
    n = 1
    
    for k in range(4):
        dx = r + nx[k]
        dy = c + ny[k]
        if 0 <= dx < 7 and 0 <= dy < 7 and arr[dx][dy] == prior and visited[dx][dy] == 0:
            n += dfs(dx, dy, arr[dx][dy])
        
    return n

cnt = 0
arr = []
nx = [0, 0, -1, 1]
ny = [-1, 1, 0, 0]
visited = [[0 for _ in range(7)] for _ in range(7)]

for _ in range(7):
    arr.append(list(map(int, input().split())))
    
for i in range(7):
    for j in range(7):
        if not visited[i][j]:
            if dfs(i, j, arr[i][j]) >= 3:
                cnt += 1
print(cnt)
            
