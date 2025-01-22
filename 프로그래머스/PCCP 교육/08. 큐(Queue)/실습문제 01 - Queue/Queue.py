import queue
que = queue.Queue()

for i in range(int(input())):
    cmd = list(input().strip().split())
    if cmd[0] == "i":
        que.put(int(cmd[1]))
    elif cmd[0] == "c":
        print(que.qsize())
    elif cmd[0] == "o":
        if que.empty():
            print("empty")
        else:
            print(que.get())
