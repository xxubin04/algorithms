import sys

n = int(input())
towers = list(map(int, sys.stdin.readline().split()))
stk =  [(0, towers[0])]
answer = [0] * n

for t in range(1, n):
    while stk:
        if towers[t] <= stk[-1][1]:
            answer[t] = stk[-1][0] + 1
            break
        else:
            stk.pop()
    stk.append((t, towers[t]))

print(*answer)