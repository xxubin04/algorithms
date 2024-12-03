from collections import deque
input = open(0).readline

num = int(input())
length = int(input())
friendship = [[] for _ in range(num+1)]
visited = [0 for _ in range(num+1)]
q = deque([(1, 0)])
cnt = 1

for n in range(length):
    a, b = map(int, input().split())
    friendship[a].append(b)
    friendship[b].append(a)
    
def bfs(visited, cnt):
    while q:
        friend = q.popleft()
        f, c = friend[0], friend[1]
        if not visited[f] and c <= 2:
            visited[f] = 1
            for i in friendship[f]:
                q.append((i, c+1))

bfs(visited, cnt)
print(sum(visited)-1)