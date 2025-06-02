import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
stk = []
nge = []

for cur in nums[::-1]:
    while stk:
        if cur < stk[-1]:
            nge.append(stk[-1])
            break
        else:
            stk.pop()
    else:
        nge.append(-1)
    stk.append(cur)

print(*reversed(nge))