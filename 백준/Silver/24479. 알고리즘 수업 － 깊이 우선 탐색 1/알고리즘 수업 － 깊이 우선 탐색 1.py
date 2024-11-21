import sys
sys.setrecursionlimit(10**6)
input = open(0).readline

num = 1

def dfs(node, nodes, visited, num):
    visited[node-1] = num
    num += 1
    for i in sorted(nodes[node-1]):
        if not visited[i-1]:  # 방문한 적이 없다면
            num = dfs(i, nodes, visited, num)

    return num

node_cnt, edge_cnt, start_node = map(int, input().split())
nodes = [[] for _ in range(node_cnt)]
visited = [0 for _ in range(node_cnt)]

for i in range(edge_cnt):
    a, b = map(int, input().split())
    nodes[a-1].append(b)
    nodes[b-1].append(a)

dfs(start_node, nodes, visited, num)

for n in visited:
    print(n)