def dfs(arr, r, c, visited):
    nx = [0, 0, -1, 1]
    ny = [1, -1, 0, 0]
    if 0 <= r < height and 0 <= c < width and not visited[r][c] and arr[r][c] == 1:
        visited[r][c] = 1
        for j in range(4):
            dfs(arr, r+nx[j], c+ny[j], visited)
    
    return visited
    

arr=[]
width, height = map(int, input().split())
for i in range(height):
    arr.append(list(map(int, input().split())))
row, col = map(int, input().split())

visited = [[0 for _ in range(width)] for _ in range(height)]

dfs(arr, row, col, visited)

for a in range(height):
    for b in range(width):
        print(visited[a][b], end=" ")
    print("")
