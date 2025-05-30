import sys

heights = []

for i in range(n := int(sys.stdin.readline())):
    heights.append(int(sys.stdin.readline()))

stk = []
cnt = 0

for h in heights:
    while stk and stk[-1] <= h:
        stk.pop()
    cnt += len(stk)
    stk.append(h)

print(cnt)