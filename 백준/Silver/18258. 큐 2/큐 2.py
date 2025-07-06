from collections import deque
import sys

q = deque()

for i in range(n := int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:  # push
        q.append(cmd[1])
    elif cmd[0] == 'pop' and len(q) == 0:
        print(-1)
    elif cmd[0] == 'pop' and len(q) != 0:
        print(q.popleft())
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty' and len(q) == 0:
        print(1)
    elif cmd[0] == 'empty' and len(q) != 0:
        print(0)
    elif cmd[0] == 'front' and len(q) == 0:
        print(-1)
    elif cmd[0] == 'front' and len(q) != 0:
        print(q[0])
    elif cmd[0] == 'back' and len(q) == 0:
        print(-1)
    elif cmd[0] == 'back' and len(q) != 0:
        print(q[-1])