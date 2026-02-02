from collections import deque

input = open(0).readline()
F, S, G, U, D = map(int, input.split())
q = deque([(S, 0)])
visited = [0 for _ in range(F+1)]
visited[S] = 1

while q:
    floor, count = q.popleft()

    if floor == G:
        print(count)
        break

    if (up := floor + U) <= F and visited[up] == 0:
        visited[up] = 1
        q.append((up, count + 1))

    if (down := floor - D) >= 1 and visited[down] == 0:
        visited[down] = 1
        q.append((down, count + 1))
else:
    print("use the stairs")