import sys

op = []
stk = []
next_num = 1

for i in range(n := int(sys.stdin.readline())):
    target = int(sys.stdin.readline())
    while next_num <= target:
        stk.append(next_num)
        op.append('+')
        next_num += 1

    if stk[-1] == target:
        stk.pop()
        op.append('-')
    else:
        print("NO")
        exit()

for p in op: print(p)