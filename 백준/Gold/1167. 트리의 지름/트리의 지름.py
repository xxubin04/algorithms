from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = open(0).readline

node = int(input())
tree = [[] for _ in range(node+1)]

for i in range(node):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

def BFS(start):
    q = deque()
    q.append((start, 0))
    visited = [-1]*(node+1)
    visited[start] = 0
    res = [0, 0]

    while q:
        cnt_node, cnt_dist = q.popleft()
        for adj_node, adj_dist in tree[cnt_node]:
            if visited[adj_node] == -1:
                cal_dist = cnt_dist + adj_dist
                q.append((adj_node, cal_dist))
                visited[adj_node] = cal_dist
                if res[1] < cal_dist:
                    res[0] = adj_node
                    res[1] = cal_dist
    return res

point, _ = BFS(1)
print(BFS(point)[1])