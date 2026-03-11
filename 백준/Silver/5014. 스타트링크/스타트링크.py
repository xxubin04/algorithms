from collections import deque
input = open(0).readline

F, S, G, U, D = map(int, input().split())
q = deque([(S, 0)])
visited = [0] * (F+1)

def bfs(loc):
    visited[loc] = 1
    while q:
        floor, cnt = q.popleft()
        if floor == G:
            return cnt

        if 1 <= (u := floor+U) <= F and not visited[u]:
            visited[u] = 1
            q.append((u, cnt+1))
        if 1 <= (d := floor-D) <= F and not visited[d]:
            visited[d] = 1
            q.append((d, cnt+1))

    return "use the stairs"

print(bfs(S))