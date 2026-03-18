from collections import deque
input = open(0).readline

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(sangguen, conv, fest, c):
    q = deque()
    q.append(sangguen)

    visited = [False] * c

    while q:
        x, y = q.popleft()

        if dist((x, y), fest) <= 1000:
            return "happy"

        for i in range(c):
            if not visited[i]:
                if dist((x, y), conv[i]) <= 1000:
                    visited[i] = 1
                    q.append(conv[i])
    return "sad"

t = int(input())
for _ in range(t):
    c = int(input())
    conv = []

    for i in range(c + 2):
        if i == 0:
            sangguen = tuple(map(int, input().split()))
        elif 1 <= i <= c:
            conv.append(tuple(map(int, input().split())))
        else:
            fest = tuple(map(int, input().split()))

    print(bfs(sangguen, conv, fest, c))