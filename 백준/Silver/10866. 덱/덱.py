from collections import deque
import sys

stk = deque()

for i in range(n := int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push_back':
        stk.append(cmd[1])
    elif cmd[0] == 'push_front':
        stk.insert(0, cmd[1])
    elif cmd[0] == 'pop_back':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif cmd[0] == 'pop_front':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.popleft())
    elif cmd[0] == 'size':
        print(len(stk))
    elif cmd[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[0])
    elif cmd[0] == 'back':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])