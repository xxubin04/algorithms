from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n+1)])
cnt = 0
nums = deque(list(map(int, sys.stdin.readline().split())))

while nums:
    idx = q.index(target := nums.popleft())

    if idx == 0:
        q.popleft()
        continue
    elif idx > (len(q) // 2):
        for _ in range(idx, len(q)):
            q.appendleft(q.pop())
            cnt += 1
        q.popleft()
    else:
        for _ in range(0, idx):
            q.append(q.popleft())
            cnt += 1
        q.popleft()

print(cnt)