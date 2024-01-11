import sys
sys.setrecursionlimit(10**6)
input = open(0).readline

N = int(input())
route = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
max_dist = 0

def dfs(x=1, total_dist=0):
    global max_dist
    visited[x] = 1
    max_dist = max(max_dist, total_dist)

    for i, j in route[x]:
        if visited[i] == 0:
            dfs(i, total_dist + j)

for i in range(N - 1):
    A, B, C = map(int, input().split())
    route[A].append([B, C])
    route[B].append([A, C])

dfs()
print(max_dist)