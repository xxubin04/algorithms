from collections import deque

N, K = map(int,input().split())
q = deque([j for j in range(1, N+1)])

i = 1
while q:
    if i % K == 0:
        print(q.popleft(), end=" ")
    else:
        q.append(q.popleft())
    i += 1
