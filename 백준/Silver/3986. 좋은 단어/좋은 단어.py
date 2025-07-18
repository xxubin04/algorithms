import sys

cnt = 0

for _ in range(int(sys.stdin.readline().rstrip())):
    stk = []
    word = list(sys.stdin.readline().rstrip())
    for w in word:
        if stk and w == stk[-1]:
            stk.pop()
        else:
            stk.append(w)

    if not stk:
        cnt += 1

print(cnt)