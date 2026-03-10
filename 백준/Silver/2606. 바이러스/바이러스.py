from collections import deque
input = open(0).readline

com = int(input()); edge = int(input())
q = deque([1])
graph = [[] for _ in range(com + 1)]
visited = [False] * (com + 1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    visited[1] = True
    while q:
        node = q.popleft()
        for conn in graph[node]:
            if visited[conn] == False:
                q.append(conn)
                visited[conn] = True

bfs()
print(com - visited.count(False))