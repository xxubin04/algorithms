input = open(0).readline

n = int(input())
a, b = map(int, input().split())
relation = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for _ in range(rel := int(input())):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

def dfs(node, cnt):
    if node == b:
        return cnt

    visited[node] = 1

    for i in relation[node]:
        if visited[i] == 0:
            res = dfs(i, cnt+1)
            if res != -1:
                return res

    return -1

print(dfs(a, 0))