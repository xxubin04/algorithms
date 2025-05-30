import sys

stk = []

for i in range(n := int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "push":
        stk.append(cmd[1])
    elif cmd[0] == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif cmd[0] == "size":
        print(len(stk))
    elif cmd[0] == "top":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])
    elif cmd[0] == "empty":
        if len(stk) == 0:
            print(1)
        else:
            print(0)