from collections import deque
input = open(0).readline

user_num, user_relation = map(int, input().split())
graph = {i:[] for i in range(1, user_num+1)}
kevin_bacon = [[] for i in range(user_num)]

for i in range(user_relation):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def bacon(q):
    global cnt
    while q:
        x, cnt = q.popleft()
        cnt += 1
        for k in graph[x]:
            if visited[k] == 0:
                visited[k] = 1
                q.append((k, cnt))
                kevin_bacon[j-1].append(cnt)

for j in range(1, user_num+1):
    visited = [0] * (user_num+1)
    queue = deque([(j, 0)])
    visited[j] = 1
    cnt = 0
    bacon(queue)

for i in range(user_num):
    kevin_bacon[i] = sum(kevin_bacon[i])
print(kevin_bacon.index(min(kevin_bacon))+1)