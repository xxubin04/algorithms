input = open(0).readline
com = int(input()); edge = int(input())
graph = [[] for _ in range (com + 1)]
visited = [0] * (com + 1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(com):
    if visited[com] == 0:
        visited[com] = 1
        for i in graph[com]:
            dfs(i)

dfs(1)
print(sum(visited) - 1)