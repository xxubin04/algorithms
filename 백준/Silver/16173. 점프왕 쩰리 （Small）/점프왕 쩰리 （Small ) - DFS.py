# DFS
input = open(0).readline

n = int(input())
area = []
dx, dy = [0, 1], [1, 0]
arrive = False
visited = [[0 for _ in range(n)] for _ in range(n)]

def DFS(x, y, visited):
    global arrive
    if area[x][y] == -1:
        arrive = True
    if visited[x][y] == 0:
        visited[x][y] = 1
        for i in range(2):
            nx, ny = x + area[x][y] * dx[i], y + area[x][y] * dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                DFS(nx, ny, visited)


for i in range(n):
    area.append(list(map(int, input().split())))

DFS(0, 0, visited)
print("HaruHaru") if arrive else print("Hing")
