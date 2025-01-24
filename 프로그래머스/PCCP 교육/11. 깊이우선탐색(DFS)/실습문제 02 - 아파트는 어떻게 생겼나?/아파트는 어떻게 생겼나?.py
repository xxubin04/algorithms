def dfs(r, c):
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    
    if 0 <= r < height and 0 <= c < width and apt[r][c] == '*' and not visited[r][c]:
        visited[r][c] = 1
        for i in range(4):
            dfs(r+nx[i], c+ny[i])
            
    return visited

width, height = map(int, input().split())
apt = []
visited = [[0 for _ in range(width)] for _ in range(height)]

for _ in range(height):
    apt.append(list(input().strip()))
    
row, col = map(int, input().split())

dfs(row-1, col-1)

for a in range(height):
    for b in range(width):
        print(visited[a][b], end='')
    print("")
