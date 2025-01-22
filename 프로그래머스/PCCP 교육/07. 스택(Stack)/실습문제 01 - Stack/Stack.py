stk = []

for i in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'i':
        stk.append(cmd[1])
    elif cmd[0] == 'o':
        if len(stk) == 0:
            print("empty")
        else:
            print(stk.pop())
    else:
        print(len(stk))
