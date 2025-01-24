def dfs(r, c):
    for i in range(4):
        dx = r+nx[i]
        dy = c+ny[i]
        if 0 <= dx < height and 0 <= dy < width and not visited[dx][dy] and island_arr[dx][dy]:
            visited[dx][dy] = 1
            dfs(dx, dy)

width, height = map(int, input().split())
island_arr = []
nx = [-1, 1, 0, 0]
ny = [0, 0, -1 ,1]
cnt = 0

for _ in range(height):
    island_arr.append(list(map(int, input().split())))

visited = [[0 for _ in range(width)] for _ in range(height)]

for i in range(height):
    for j in range(width):
        if not visited[i][j] and island_arr[i][j] == 1:
            cnt += 1
            visited[i][j] = 1
            dfs(i, j)

print(cnt)
