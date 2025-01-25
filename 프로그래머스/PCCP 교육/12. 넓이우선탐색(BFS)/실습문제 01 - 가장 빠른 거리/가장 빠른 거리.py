from collections import deque

height, width = map(int, input().split())
sh, sw = map(int, input().split())
eh, ew = map(int, input().split())
visited = [[-1 for _ in range(width)] for _ in range(height)]

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

def bfs(sh, sw, eh, ew):
    q = deque([(sh, sw)])
    visited[sh][sw] = 0
    
    while q:
        x, y = q.popleft()
        if x == eh and y == ew:
            return visited[x][y]
        
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            
            if 0 <= dx < height and 0 <= dy < width and visited[dx][dy] == -1:
                visited[dx][dy] = visited[x][y] + 1
                q.append((dx, dy))

print(bfs(sh-1, sw-1, eh-1, ew-1))
