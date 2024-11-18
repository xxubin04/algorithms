from collections import deque
input = open(0).readline

num = 1
q = deque([])

def bfs(nodes, visited, num):
    while q:
        node = q.popleft()
        if not visited[node-1]:
            visited[node-1] = num
            num += 1
            for j in sorted(nodes[node-1], reverse=True):
                q.append(j)
    return visited

node_cnt, edge_cnt, start_node = map(int, input().split())
nodes = [[] for _ in range(node_cnt)]
visited = [0 for _ in range(node_cnt)]

q.append(start_node)

for i in range(edge_cnt):
    a, b = map(int, input().split())
    nodes[a-1].append(b)
    nodes[b-1].append(a)

for n in bfs(nodes, visited, num):
    print(n)